import datetime
import importlib
import random
import pathlib
import os
import shutil


if __name__ == "__main__":
    cmd_args = os.sys.argv
    run(cmd_args)


def run(*args, **kwargs):
    print("running")
    attrs = importlib.import_module(os.path.basename(__file__).split(".")[0])
    args_list = args[0]
    for n in range(1, len(args_list)):
        try:
            print(f"trying to run {args_list[n]}")
            attrs.__getattribute__(args_list[n])(args_list[n + 1:])
        except AttributeError as err:
            print(f"{err} occured. {args_list[n]} is not an attirbute of {__file__}")
        except TypeError as err:
            print(f"{err} {args_list[n]}")


def commit(MESSAGE):
    images_dir = os.path.join(file_search(os.getcwd(), ".wit"), ".wit", "images")
    wit_dir = os.path.split(images_dir)[0]
    stage_area_dir = os.path.join(os.path.split(images_dir)[0], "staging_area")
    commit_id = "".join(random.choices([*[str(n) for n in range(9)], "a", "b", "c", "d", "e"], k=40))
    commit_folder_dir = os.path.join(images_dir, commit_id)
    os.mkdir(commit_folder_dir)
    timestamp = datetime.datetime.now()
    try:
        with open(os.path.join(wit_dir, "references.txt"), "r") as file:
            parents = file.readlines(0)[0].split("=")[1]
        parents = parents
    except FileNotFoundError:
        parents = None
    finally:
        with open(os.path.join(wit_dir, "references.txt"), "w") as file:
            file.writelines([f"HEAD={commit_id}\n", f"master={commit_id}\n"])            
    with open(".".join([commit_folder_dir, "txt"]), "w+") as file:
        file.writelines([f"parent={parents}\n", f"date={timestamp}\n", f"message={MESSAGE}\n"])
    shutil.copytree(stage_area_dir, os.path.join(commit_folder_dir, "staging_area"))        


def file_search(directory, search_value):
    if not os.path.exists(directory):
        print("did not find directory")
        raise FileNotFoundError
    if os.path.isdir(directory):
        dir_to_check = directory
    else:
        dir_to_check = os.path.split(directory)[0]
    n = True
    while n:
        if search_value not in os.listdir(dir_to_check):
            dir_to_check = str(list(os.path.split(dir_to_check))[0])
        elif search_value in os.listdir(dir_to_check):
            print(f"{search_value} found in one of the directories of {directory}")
            return Path(dir_to_check)
        elif not list(os.path.split(dir_to_check))[0]:
            print(f"no {search_value} file found in directories")
            n == False
            raise FileNotFoundError


def init(*args, **kwargs): 
    print("running init")
    try:
        os.mkdir(".wit")
        wit_dir = r".wit"
        print("created .wit dir")
    except FileExistsError:
        wit_dir = r".wit"
        print(f".wit folder not created-exists already in current working directory")
    try:
        os.mkdir(os.path.join(wit_dir, "images"))
        print("images directory created")
    except FileExistsError:
        print(f"images dir not created-exists already in {wit_dir} working directory")
    try:
        os.mkdir(os.path.join(wit_dir, "staging_area"))
        print("staging_area dir created")
    except FileExistsError:
        print(f"staging_area file not created-exists already in {wit_dir} working directory")


def add(*args, **kwargs):
    arg_root = args[0][0]
    if not os.path.exists(arg_root):
        if not os.path.exists(os.path.join(os.getcwd, arg_root)):
            print(f"{arg_root} does not exist")
            raise FileNotFoundError
        else:
            arg_root = os.path.join(os.getcwd(), arg_root)
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
    print("add performed successfuly")

  
def test(*args, **kwargs):
    print("in test")
    [print(n) for n in args]
    return True




