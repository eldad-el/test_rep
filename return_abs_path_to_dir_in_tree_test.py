import os


def dir_check(directory, search_value):
    if not os.path.exists(directory):
        if not os.path.exists(os.path.join(os.getcwd(), directory)):
            print(f"{directory} does not exist")
            raise FileNotFoundError
        else:
            directory = os.path.join(os.getcwd(), directory)
    if os.path.isdir(directory):
        dir_to_check = directory
    else:
        dir_to_check = os.path.split(directory)[0]
    n = 0
    while n == 0:
        if search_value not in os.listdir(dir_to_check):
            dir_to_check = str(list(os.path.split(dir_to_check))[0])
        elif search_value in os.listdir(dir_to_check):
            print(f"{search_value} found in one of the directories of {directory}")
            return dir_to_check
        elif not list(os.path.split(dir_to_check))[0]:
            print(f"no {search_value} file found in directories")
            raise FileNotFoundError
    