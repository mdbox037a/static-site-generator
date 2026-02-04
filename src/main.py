import sys
from copystatic import copy_static
from gencontent import generate_pages_recursive


def main() -> None:
    if sys.argv[1]:
        basepath = sys.argv[1]
    else:
        basepath = "/"

    source_dir_path = "./content/"
    static_dir_path = "./static"
    dest_dir_path = "./docs/"
    template_path = "./template.html"

    copy_static(static_dir_path, dest_dir_path)
    generate_pages_recursive(basepath, source_dir_path, template_path, dest_dir_path)


if __name__ == "__main__":
    main()
