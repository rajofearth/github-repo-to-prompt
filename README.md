# GitHub Repo to LLM Prompt

## Description

A web application that fetches the contents of a GitHub repository and generates a structured prompt for large language models (LLMs).

## Features

- Fetches repository contents using GitHub API.
- Generates a tree-like structure of the repository.
- Includes file contents in the prompt.
- Easy-to-use web interface.

## Prerequisites

- Python 3.7 or higher
- Flask, requests, python-dotenv libraries
- A GitHub Personal Access Token

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/rajofearth/github-repo-to-prompt.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Obtain a GitHub Personal Access Token and save it in a `.env` file:
   ```
   GITHUB_TOKEN=your_token_here
   ```
4. Add `.env` to `.gitignore` to prevent it from being tracked:
   ```bash
   echo ".env" >> .gitignore
   ```

## Usage

1. Run the app:
   ```bash
   python app.py
   ```
2. Open a web browser and navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/).
3. Enter a GitHub repository URL and submit to generate the prompt.

## Example Output

```
github-repo-to-prompt/
│
├── app.py
├── .env
├── requirements.txt
├── templates/
│   └── index.html
└── README.md

/app.py:
# Contents of app.py

/.env:
# GITHUB_TOKEN=your_token_here

/requirements.txt:
# Flask==2.3.2
# requests==2.31.0
# python-dotenv==1.0.0

/templates/index.html:
# Contents of index.html

/README.md:
# Contents of README.md
```

## File Structure

- `app.py`: The main Flask application.
- `.env`: Environment variables (e.g., GitHub token).
- `requirements.txt`: Python dependencies.
- `templates/`: HTML templates for the web app.
  - `index.html`: The frontend HTML file.
- `README.md`: Project documentation.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

MIT License

## Contact

For questions or feedback, contact [rajofearth@proton.me] or visit [github.com/rajofearth].

---