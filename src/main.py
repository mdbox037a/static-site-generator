from textnode import TextNode, TextType
from copystatic import copy_static
from gencontent import generate_page


def main() -> None:
    copy_static()
    generate_page("content/index.md", "template.html", "public/index.html")


if __name__ == "__main__":
    main()
