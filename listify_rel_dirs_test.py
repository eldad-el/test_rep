import os


def listify_dirs(long_path, short_path):
    dirs_to_add_str = os.path.relpath(long_path, short_path)
    split_to_check = list(os.path.split(dirs_to_add_str))
    dirs_to_add = []
    while split_to_check[1]:
        dirs_to_add.append(split_to_check.pop())
        split_to_check = list(os.path.split(str(split_to_check[0])))
    return dirs_to_add