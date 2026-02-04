import sys
from copystatic import copy_static
from gencontent import generate_pages_recursive


def main() -> None:
    if sys.argv[1]:
        basepath = sys.argv[1]
    else:
        basepath = "/"

    copy_static()
    generate_pages_recursive(basepath, "content/", "template.html", "public/")


if __name__ == "__main__":
    main()
