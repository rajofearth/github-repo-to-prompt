# GitHub Repo to LLM Prompt

## Description

A Streamlit web application that fetches the contents of a GitHub repository and generates a structured prompt for large language models (LLMs).

- View it live [here](https://gh-repo-to-prompt.streamlit.app/)

## Features

- Fetches repository contents using GitHub API.
- Generates a tree-like structure of the repository.
- Includes file contents in the prompt.
- User-friendly interface with sidebar for settings.

## Prerequisites

- Python 3.7 or higher
- Streamlit, requests libraries
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
3. Obtain a GitHub Personal Access Token and save it in `api_key.txt`(Optional):
   ```
   your_token_here
   ```
4. Add `api_key.txt` to `.gitignore` to prevent it from being tracked.

## Usage

1. Run the app:
   ```bash
   streamlit run app_streamlit.py
   ```
2. Open a web browser and navigate to [http://localhost:8501/](http://localhost:8501/).
3. Enter a GitHub repository URL and submit to generate the prompt.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

MIT License

## Contact

For questions or feedback, contact [rajofearth@proton.me] or visit [github.com/rajofearth].
