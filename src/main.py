from textnode import TextNode, TextType
from copystatic import copy_static
from gencontent import generate_page, generate_pages_recursive


def main() -> None:
    copy_static()
    generate_pages_recursive("content/", "template.html", "public/")


if __name__ == "__main__":
    main()
