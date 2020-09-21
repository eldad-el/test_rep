from pathlib import Path
import os


wit_dir = Path(r"C:\Users\Eldad\Documents\study\python\week_10\.wit")
wit_dir_str = wit_dir.__str__()

files_tree = {}

#for directory, folders, files in os.walk(wit_dir):
#    files_tree[Path(directory).parent()] = 