frontmatter_prompt = """

Given the following partial frontmatter:

{frontmatter}

And the following content of a blog post written in markdown:

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
    "description": "A description of the post within 100 words (summarize based on the content of the post)",
    "categories": ["List of categories, use simple words, and as short as possible"],
    "tags": ["List of tags use simple words, and as short as possible"],
    "math": True/False, # if you found any latex in the content, set to true, otherwise set to false
    "draft": True/False # if you think the post is very rough and needs to be polished, set to true, otherwise set to false
}}

"""


