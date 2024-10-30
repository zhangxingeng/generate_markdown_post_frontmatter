index_prompt = """

Given the following partial frontmatter (if the frontmatter is empty, you should create all fields):

{frontmatter}

And the following blog posts names:

{content}

Please generate the full frontmatter for the blog post in json format.
Make sure the original frontmatter is included in the new frontmatter.
Please make sure the JSON is properly formatted and valid.
Do not include any other text than the JSON.
All fields should be created, even if the value is an empty string or empty list or anything else.
Make sure the output is parsable by json.loads(). For example, True, False, and None keywords should be quoted.

Example output with valid JSON format:

{{
    "title": "Title of the post (summarize based on the content of the post)",
    "summary": "A summary of the posts inside this folder",
    "description": "A description of what this folder is about",
}}

"""


