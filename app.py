from flask import Flask, request, render_template
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

def fetch_all_files(url, base_path, token=None):
    headers = {"Authorization": f"token {token}"} if token else {}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    contents = response.json()
    files = []
    for item in contents:
        if item["type"] == "file":
            file_content_response = requests.get(item["download_url"], headers=headers)
            file_content_response.raise_for_status()
            content = file_content_response.text
            file_path = f"{base_path}/{item['name']}".lstrip('/')
            files.append((file_path, content))
        elif item["type"] == "dir":
            files.extend(fetch_all_files(item["url"], f"{base_path}/{item['name']}", token))
    return files

class TreeNode:
    def __init__(self, name, is_dir=False):
        self.name = name
        self.is_dir = is_dir
        self.children = []
        self.content = None  # For files

def build_tree(file_paths):
    root = TreeNode("", is_dir=True)
    for file_path, content in file_paths:
        parts = file_path.split('/')
        current = root
        for part in parts[:-1]:
            found = False
            for child in current.children:
                if child.name == part and child.is_dir:
                    current = child
                    found = True
                    break
            if not found:
                dir_node = TreeNode(part, is_dir=True)
                current.children.append(dir_node)
                current = dir_node
        file_node = TreeNode(parts[-1], is_dir=False)
        file_node.content = content
        current.children.append(file_node)
    return root

def generate_tree_structure(root, tree_lines, depth=0, last=True):
    indent = ' ' * depth * 2
    if depth > 0:
        if last:
            prefix = '└── '
            indent = indent[:-2] + '   '
        else:
            prefix = '├── '
            indent = indent[:-2] + '│  '
    else:
        prefix = ''
    if root.is_dir:
        tree_lines.append(f"{indent}{prefix}{root.name}/")
    else:
        tree_lines.append(f"{indent}{prefix}{root.name}")
    for i, child in enumerate(root.children):
        is_last = (i == len(root.children) - 1)
        generate_tree_structure(child, tree_lines, depth + 1, is_last)

def generate_prompt(file_paths):
    tree_lines = []
    root = build_tree(file_paths)
    generate_tree_structure(root, tree_lines)
    prompt = "\n".join(tree_lines) + "\n\n"
    for file_path, content in file_paths:
        prompt += f"/{file_path}:\n{content}\n\n"
    return prompt

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        repo_url = request.form["repo_url"]
        parts = repo_url.strip("/").split("/")
        owner, repo = parts[-2], parts[-1]
        url = f"https://api.github.com/repos/{owner}/{repo}/contents"
        try:
            file_paths = fetch_all_files(url, "", GITHUB_TOKEN)
            prompt = generate_prompt(file_paths)
            return render_template("index.html", prompt=prompt)
        except Exception as e:
            return render_template("index.html", error=str(e))
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)