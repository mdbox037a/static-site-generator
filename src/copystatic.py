import os
import shutil


def copy_static():
    """Copy all contents of the src dir into the dst dir"""
    src_dir = os.path.abspath("static")
    dst_dir = os.path.abspath("public")
    if os.path.exists(dst_dir):
        shutil.rmtree(dst_dir)

    copy_files_recursive(src_dir, dst_dir)


def copy_files_recursive(src_dir: str, dst_dir: str):
    if not os.path.exists(dst_dir):
        os.mkdir(dst_dir)
    for entry in os.listdir(src_dir):
        from_path = os.path.join(src_dir, entry)
        dest_path = os.path.join(dst_dir, entry)
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files_recursive(from_path, dest_path)
