import os
import pathlib
from markdown_blocks import markdown_to_html_node


def extract_title(markdown: str) -> str:
    """
    Detect the h1 header in markdown input (the line beginning with '#') and
    return the header as a string
    """
    lines = markdown.splitlines()
    for line in lines:
        clean_line = line.strip()
        if clean_line.startswith("# "):
            return clean_line[2:].strip()
    raise Exception("No h1 detected: invalid document for site conversion")


def generate_page(
    basepath: str, from_path: str, template_path: str, dest_path: str
) -> None:
    """
    Accept contents of a markdown file as source for static site and convert its
    contents into an html document; store the new html document in dest_path
    """
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as md:
        markdown_file = md.read()
    with open(template_path, "r") as t:
        template_file = t.read()

    if "{{ Title }}" not in template_file:
        raise ValueError("Template file missing {{ Title }} placeholder")
    if "{{ Content }}" not in template_file:
        raise ValueError("Template file missing {{ Content }} placeholder")

    html_title_string = extract_title(markdown_file)
    html_content_string = markdown_to_html_node(markdown_file).to_html()
    index_html = (
        template_file.replace("{{ Title }}", html_title_string)
        .replace("{{ Content }}", html_content_string)
        .replace('href="/', f'href="{basepath}')
        .replace('src="/', f'src="{basepath}')
    )

    dst_dir = os.path.dirname(dest_path)
    if dst_dir != "":
        os.makedirs(dst_dir, exist_ok=True)

    with open(dest_path, "w") as index:
        index.write(index_html)


def generate_pages_recursive(
    basepath: str, dir_path_content: str, template_path, dest_dir_path
) -> None:
    """
    Crawl every entry in the content/ directory and generate a new .html file
    for each .md file, written to public/ with the same dir structure as in content/
    """

    content_items = os.listdir(dir_path_content)
    for item in content_items:
        item_src_path = os.path.join(dir_path_content, item)
        # print(f"DEBUG: {item_src_path}")
        item_dst_path = os.path.join(dest_dir_path, item.replace(".md", ".html"))
        # print(f"DEBUG: {item_dst_path}")
        if item.endswith(".md"):
            generate_page(basepath, item_src_path, template_path, item_dst_path)
        elif os.path.isfile(item):
            continue
        else:
            generate_pages_recursive(
                basepath, item_src_path, template_path, item_dst_path
            )
