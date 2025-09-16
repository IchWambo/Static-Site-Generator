import os
from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")
    from_path_markdown = ""
    template = ""
    with open(f"{from_path}", "r") as file:
        content = file.read()
        from_path_markdown = content
    with open(f"{template_path}", "r") as file:
        content = file.read()
        template = content
    html_node = markdown_to_html_node(from_path_markdown)
    html = html_node.to_html()
    title = extract_title(from_path_markdown)
    page = template.replace("{{ Title }}", title).replace("{{ Content }}", html)
    dirpath = os.path.dirname(dest_path)
    if dirpath:
        os.makedirs(dirpath, exist_ok=True)
    with open(f"{dest_path}", "w") as file:
        file.writelines(page)
    
