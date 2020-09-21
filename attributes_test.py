import importlib
import pathlib
import os
import shutil



if __name__ == "__main__":
    attrs = importlib.import_module(os.path.basename(__file__).split(".")[0])
    a = attrs.__dict__.items()[0][0]
    print(type(attrs))
    attrs.__getattribute__(a)
    pass



None