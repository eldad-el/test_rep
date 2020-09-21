import datetime
import os
import pathlib
import importlib
import shutil
import random
import itertools
from wit import file_search


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
    return wit_dir


wit_dir = commit("dude")



