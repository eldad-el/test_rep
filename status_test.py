import datetime
import os
from pathlib import Path
import importlib
import shutil
import random
from wit import file_search


def status(wit_dir=file_search(Path.cwd(), ".wit")):
    with Path.joinpath(wit_dir, "references,txt").open() as references_path:
        current_commit_id = references_path.readline().split("=")[1]
    stage_dir = Path.joinpath(wit_dir, "staging_area")
    images_dir = Path.joinpath(wit_dir, "images")
    changetime_files_dict = {stage_dir: [], images_dir: []}
    for a, _, c in Path.cwd():
        for file in c:
            if images_dir in a:
                changetime_files_dict[images_dir].append({os.path.join(a, c): os.path.getctime(os.path.join(a, c)))
            elif stage_dir in a:
                changetime_files_dict[stage_dir].append({os.path.join(a, c): os.path.getctime(os.path.join(a, c)))
    stage_changetimes, images_changetimes = changetime_files_dict
    
    for file in stage_changetimes:
        n = stage_changetimes[file] > images_changetimes[file]
        if n:
            print(f"")


    

status()