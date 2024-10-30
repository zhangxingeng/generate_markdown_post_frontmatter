# Standard library imports
import argparse
from datetime import datetime, timedelta
import json
from pathlib import Path
import random
import re
import shutil

# Third-party imports
from dotenv import load_dotenv
import frontmatter
from frontmatter import Post
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI


def generate_random_date(start_date_str, end_date_str):
    ''' find a random datetime between start_date and end_date '''
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
    end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
    delta = end_date - start_date
    random_days = random.randrange(delta.days + 1)
    random_date = start_date + timedelta(days=random_days)
    return random_date.strftime('%Y-%m-%d')


def generate_front_matter(content: str, frontmatter: str, prompt_str: str):
    promptTemplate = PromptTemplate.from_template(prompt_str)
    prompt = promptTemplate.format(content=content, frontmatter=frontmatter)
    res = llm.invoke(prompt)
    return parse_json(res)


def parse_json(text: str) -> dict:
    text = re.sub(r'\bTrue\b', 'true', text)
    text = re.sub(r'\bFalse\b', 'false', text)
    text = re.sub(r'\bNone\b', 'null', text)
    try:
        res = json.loads(text)
        return res
    except Exception as e:
        print(f'Error parsing json: {e}, original text: {text}')
        raise e


def front_matter_stringify(front_matter: dict[str, object]) -> str:
    res = {}
    for key, value in front_matter.items():
        if isinstance(value, datetime):
            res[key] = value.strftime('%Y-%m-%d')
        else:
            res[key] = str(value)
    return json.dumps(res)


def post_additional_data(post: Post):
    if 'date' not in post.metadata:
        post.metadata['date'] = generate_random_date(
            '2024-01-01', '2024-10-30')
    if 'params' not in post.metadata:
        post.metadata['params'] = {}
    if 'author' not in post.metadata['params']:
        post.metadata['params']['author'] = 'Shane Zhang'


def read_markdown_file(in_path: Path) -> Post:
    with open(in_path, 'r', encoding='utf-8') as f:
        post = frontmatter.load(f)
    return post


def write_markdown_file(post: Post, out_path: Path):
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(frontmatter.dumps(post))


def process_index_file(post: Post, file_names: list[str]) -> Post:
    from literals import index_prompt
    content_str = ', '.join(file_names)
    front_matter_str = front_matter_stringify(post.metadata)
    new_front_matter = generate_front_matter(
        content_str, front_matter_str, index_prompt)
    post.metadata.update(new_front_matter)
    return post


def process_post_file(post: Post) -> Post:
    from literals import frontmatter_prompt
    content_str = post.content
    front_matter_str = front_matter_stringify(post.metadata)
    new_front_matter = generate_front_matter(
        content_str, front_matter_str, frontmatter_prompt)
    post.metadata.update(new_front_matter)
    post_additional_data(post)
    return post

def process_folder_recursive(src_folder: Path, dst_folder: Path):
    '''Process all markdown files in the src_folder and save to dst_folder'''
    skip_posts = True # for debugging
    skip_index = True # for debugging
    dst_folder.mkdir(parents=True, exist_ok=True)
    for item in src_folder.iterdir():
        src_item_path = src_folder / item.name
        dst_item_path = dst_folder / item.name

        if item.is_dir():
            # Create the destination directory if it doesn't exist
            dst_item_path.mkdir(parents=True, exist_ok=True)
            folder_files = [child.name for child in src_item_path.iterdir()]
            if not skip_index and '_index.md' in folder_files:
                index_file = src_item_path / '_index.md'
                index_post = read_markdown_file(index_file)
                index_post = process_index_file(index_post, folder_files)
                write_markdown_file(index_post, dst_item_path / '_index.md')
            # Recursively process the subdirectory
            process_folder_recursive(src_item_path, dst_item_path)

        elif item.is_file():
            # Ensure the parent directory exists
            dst_item_path.parent.mkdir(parents=True, exist_ok=True)

            if not skip_posts and item.suffix == '.md' and item.name != '_index.md':
                # Process markdown files when skip_posts is False
                post = read_markdown_file(src_item_path)
                post = process_post_file(post)
                write_markdown_file(post, dst_item_path)
            else:
                # Copy all other files
                shutil.copy2(src_item_path, dst_item_path)


if __name__ == '__main__':
    load_dotenv()
    parser = argparse.ArgumentParser(description='Process markdown files and generate front matter.')
    parser.add_argument('src', type=str, help='Source folder containing markdown files.', required=True)
    parser.add_argument('dest', type=str, help='Destination folder to save processed files.', required=True)
    parser.add_argument('model', type=str, help='OpenAI model name', default='gpt-3.5-turbo-instruct')
    args = parser.parse_args()
    llm = OpenAI(model=args.model, temperature=0.0)
    process_folder_recursive(Path(args.src_folder), Path(args.dst_folder))