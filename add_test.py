import os
import shutil


arg_root = r"C:\Users\Eldad\Documents\study\python\week_10\test_a\test_a1\test_b\test_b1"
if not os.path.exists(arg_root):
    print("did not find directory")
    raise FileNotFoundError
if os.path.isdir(arg_root):
    dir_to_check = arg_root
else:
    dir_to_check = os.path.split(arg_root)[0]
n = 0
while n == 0:
    if ".wit" not in os.listdir(dir_to_check):
        dir_to_check = str(list(os.path.split(dir_to_check))[0])
    elif ".wit" in os.listdir(dir_to_check):
        stage_area_dir = os.path.join(dir_to_check, ".wit", "staging_area")
        n = 1
    elif not list(os.path.split(dir_to_check))[0]:
        print("no .wit file found in directories")
        raise FileNotFoundError
dirs_to_add_str = os.path.relpath(arg_root, dir_to_check)
split_to_check = list(os.path.split(dirs_to_add_str))
dirs_to_add = []
while split_to_check[1]:
    dirs_to_add.append(split_to_check.pop())
    split_to_check = list(os.path.split(str(split_to_check[0])))
dir_to_copy = dirs_to_add[0]
dirs_to_add = dirs_to_add[1:]
current_dir = stage_area_dir
while dirs_to_add:
    try:
        os.mkdir(os.path.join(current_dir, dirs_to_add[-1]))
        current_dir = os.path.join(current_dir, dirs_to_add.pop())
    except FileExistsError:
        current_dir = os.path.join(current_dir, dirs_to_add.pop())    
shutil.copytree(arg_root, os.path.join(current_dir, dir_to_copy))
print("Done")
