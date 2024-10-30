# Generate Markdown Post Frontmatter

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/downloads/)
 
 **Disclaimer**: This document was created with the assistance of AI.

 Automatically generate comprehensive front matter for your Hugo Markdown posts using OpenAI's GPT language model. This tool simplifies the process of adding summaries, keywords, categories, and other metadata to your posts, saving you time and ensuring consistency across your blog.

## Table of Contents

- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Setting Up the Environment](#setting-up-the-environment)
- [Setup](#setup)
  - [OpenAI API Key](#openai-api-key)
- [Usage](#usage)
  - [Basic Command](#basic-command)
  - [Command-Line Arguments](#command-line-arguments)
  - [Examples](#examples)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
  - [Development Setup](#development-setup)
  - [Submitting Changes](#submitting-changes)
- [License](#license)
- [Contact](#contact)
- [Acknowledgments](#acknowledgments)

## Features

- **Automated Front Matter Generation**: Uses GPT-3.5 to generate `title`, `summary`, `description`, `categories`, `tags`, and more.
- **Recursive Directory Processing**: Processes all Markdown files in a directory tree, including `_index.md` files.
- **Customizable**: Easily skip processing of individual posts or index files with command-line flags.
- **Extensible**: Written in Python with clear code structure, making it easy to modify or extend.

## Demo

![Demo GIF](demo.gif)

*Above: A demonstration of the tool processing a directory of Markdown files and generating front matter automatically.*

## Installation

### Prerequisites

- **Python 3.7+**: Ensure you have Python installed. You can download it from the [official website](https://www.python.org/downloads/).
- **OpenAI Account**: You'll need an API key from OpenAI. Sign up [here](https://platform.openai.com/signup).

### Setting Up the Environment

1. **Clone the Repository**

   ```bash
   git clone https://github.com/zhangxingeng/generate_markdown_post_frontmatter.git
   cd generate_markdown_post_frontmatter
   ```

2. **(Optional) Create a Virtual Environment**

   It's a good practice to use a virtual environment to manage dependencies.

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   Install the required packages using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

   **Note**: The `requirements.txt` file includes:

   - `openai`
   - `python-dotenv`
   - `langchain`
   - `frontmatter`
   - Any other necessary packages.

## Setup

### OpenAI API Key

1. **Get an OpenAI API Key**

   - Sign up or log in to your OpenAI account.
   - Navigate to the **API Keys** section:
     - Click on your profile icon in the top-right corner.
     - Select **View API Keys** from the dropdown menu.
     - Click on **Create new secret key**.
     - Copy the generated API key.

2. **Create a `.env` File**

   In the root directory of the project, create a file named `.env` and add your OpenAI API key:

   ```plaintext
   OPENAI_API_KEY=<your_openai_api_key_here>
   ```

   **Important**: Do not share this key publicly. Ensure that your `.env` file is included in your `.gitignore` to keep your API key secure.

## Usage

### Basic Command

To generate the front matter for your Hugo Markdown posts, use the following command:

```bash
python main.py <src_folder> <dst_folder>
```

- `<src_folder>`: Path to the source directory containing your Markdown files.
- `<dst_folder>`: Path to the destination directory where processed files will be saved.

### Command-Line Arguments

- `--skip_posts`: Skip processing of individual post files (only process `_index.md` files).
- `--skip_index`: Skip processing of `_index.md` files.
- `-h`, `--help`: Show help message and exit.

**Example:**

```bash
python main.py ./content/posts/ ./content/posts_gen/
```

### Examples

1. **Process All Files**

   Process both `_index.md` files and individual post files:

   ```bash
   python main.py ./content/posts/ ./content/posts_gen/
   ```

2. **Skip Individual Posts**

   Only process `_index.md` files:

   ```bash
   python main.py ./content/posts/ ./content/posts_gen/ --skip_posts
   ```

3. **Skip Index Files**

   Only process individual post files:

   ```bash
   python main.py ./content/posts/ ./content/posts_gen/ --skip_index
   ```

4. **Display Help**

   Show all available command-line options:

   ```bash
   python main.py -h
   ```

### Output

- Processed files will be saved in the specified destination directory, maintaining the same directory structure.
- Original files are not modified.

## How It Works

The tool performs the following steps:

1. **Load Environment Variables**

   Loads the OpenAI API key from the `.env` file using `python-dotenv`.

2. **Initialize OpenAI Language Model**

   Uses the `langchain` library to interact with the OpenAI GPT-3.5 model.

3. **Recursive Directory Traversal**

   - Walks through the source directory tree.
   - Processes `_index.md` files and individual Markdown posts based on the provided flags.

4. **Front Matter Generation**

   - Reads existing front matter and content from each Markdown file.
   - Generates new front matter by prompting the language model with the content.
   - Merges the original and generated front matter.

5. **File Writing**

   - Writes the updated Markdown files to the destination directory.
   - Copies non-Markdown files (e.g., images) to the destination directory.

## Contributing

We welcome contributions to this project! Whether it's reporting a bug, adding a feature, or improving documentation, your input is valuable.

### Development Setup

1. **Fork the Repository**

   Click on the **Fork** button at the top-right corner of the repository page.

2. **Clone Your Fork**

   ```bash
   git clone https://github.com/<your_username>/generate_markdown_post_frontmatter.git
   cd generate_markdown_post_frontmatter
   ```

3. **Create a New Branch**

   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Install Development Dependencies**

   In addition to the standard requirements, install any development tools you need, such as linters or formatters.

   ```bash
   pip install black flake8
   ```

### Submitting Changes

1. **Make Your Changes**

   - Ensure code is well-documented.
   - Follow the existing coding style.

2. **Run Tests**

   If tests are available, run them to ensure nothing is broken.

   ```bash
   pytest
   ```

3. **Commit Changes**

   ```bash
   git add .
   git commit -m "Add feature XYZ"
   ```

4. **Push to Your Fork**

   ```bash
   git push origin feature/your-feature-name
   ```

5. **Open a Pull Request**

   - Go to the original repository.
   - Click on **New Pull Request**.
   - Select your branch and create the pull request.
   - Provide a clear description of your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions, suggestions, or issues, please feel free to reach out:

- **Email**: [zhangxingeng970221@gmail.com](mailto:zhangxingeng970221@gmail.com)
- **GitHub Issues**: [Create an Issue](https://github.com/zhangxingeng/generate_markdown_post_frontmatter/issues)

## Acknowledgments

- **OpenAI**: For providing the powerful GPT language model.
- **LangChain**: For simplifying interactions with LLMs.
- **Contributors**: Thank you to all the contributors who have improved this project.

---

*Thank you for using this project! We hope it makes your workflow more efficient and enjoyable. If you like it, please give it a star on GitHub!* ⭐

# Additional Documentation

To further assist users and contributors, here are more detailed explanations of certain aspects of the project.

## Detailed Functionality

### Front Matter Fields Generated

The tool generates the following fields in the front matter:

- `title`: Summarized from the content.
- `summary`: A brief summary of the post.
- `description`: A more detailed description.
- `categories`: A list of relevant categories.
- `tags`: A list of tags.
- `math`: Indicates if mathematical expressions are present.
- `draft`: Indicates if the post is a draft.

### Prompt Templates

Custom prompt templates are used to guide the language model in generating the front matter. These templates ensure consistency and accuracy in the generated metadata.

### Error Handling

- **JSON Parsing**: The tool includes robust parsing to handle JSON output from the language model, replacing Python-specific boolean and null values with JSON-compatible ones.
- **File Operations**: Checks are in place to ensure directories exist before writing files, and errors are logged for troubleshooting.

## FAQ

### Why do I need an OpenAI API key?

The tool uses OpenAI's GPT language model to generate front matter based on your content. An API key is required to authenticate your requests.

### Is my content sent to OpenAI servers?

Yes, the content of your Markdown files is sent to OpenAI's API to generate the front matter. Please ensure that you are comfortable with this and comply with OpenAI's [Usage Policies](https://openai.com/policies/usage-policies).

### Can I use a different language model?

The code is designed to use OpenAI's GPT models via the `langchain` library. However, you can modify the code to use a different model or provider supported by `langchain`.

### How do I customize the prompt templates?

The prompt templates are defined in the `literals` directory. You can edit the `frontmatter_prompt.py` and `index_prompt.py` files to customize the prompts used.

## Troubleshooting

### Common Issues

- **API Key Errors**: Make sure your `.env` file contains the correct OpenAI API key.
- **Permission Errors**: Ensure you have read/write permissions for the source and destination directories.
- **Python Version**: The tool requires Python 3.7 or higher.

### Getting Help

If you encounter issues, you can:

- Check the [GitHub Issues](https://github.com/zhangxingeng/generate_markdown_post_frontmatter/issues) to see if it's a known problem.
- Open a new issue with detailed information about the problem.

## Best Practices

- **Version Control**: Keep your source Markdown files under version control (e.g., Git) to track changes and revert if necessary.
- **Backups**: Always backup your data before running bulk operations.
- **API Usage**: Be mindful of the OpenAI API usage limits and costs associated with making API calls.

## Future Plans

- **Add Tests**: Implement unit tests to ensure code reliability.
- **Plugin System**: Develop a plugin system to allow custom processing steps.
- **GUI Application**: Create a graphical interface for users who prefer not to use the command line.
- **Docker Support**: Provide a Dockerfile for easy containerization.

## Learning Resources

- **OpenAI API Documentation**: [Link](https://platform.openai.com/docs/introduction)
- **LangChain Documentation**: [Link](https://langchain.readthedocs.io/en/latest/)
- **Hugo Front Matter**: [Link](https://gohugo.io/content-management/front-matter/)

---

*This README was last updated on [Date]. Please refer to the repository for the most recent updates.*