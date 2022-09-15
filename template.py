from genericpath import exists
import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s: ')

package_name  = "deepClassifier"

list_of_file = [
    ".github/workflow/.gitkeep",# help to keep an emply folder , since you cant push emplty folder to remote repo.
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/components/__init__py",# create script file 
    f"src/{package_name}/utils/__init__py",# create script file
    f"src/{package_name}/constants/__init__py",# create script file 
    f"src/{package_name}/pipline/__init__py", #create script file
    f"src/{package_name}/entity/__init__py", #create script file 
    f"src/{package_name}/config/__init__py", #create script file
    "tests/__init__.py",
    "tests/unit/__init__.py", # to test a specific component
    "tests/integration/__init__.py", # to test intesctions of two Component.
    "configs/config.yaml",
    "dvc.yaml",
    "param.yaml",
    "init_setup.sh",# a shell script file, hel[s to create venv
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",# for creating python package not for production 
    "pyproject.toml", # for creating python package not for production
    "tox.ini", # for testing the package localy
    "research/trials.ipynb" # a jupyter note for testing anfd try

    ]

for file in list_of_file:
    filepath = Path(file)
    dir,file_name = os.path.split(filepath)
    if dir != "":
        os.makedirs(dir,exist_ok=True)
        logging.info(f"create dir {dir} for file {file_name}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,"w") as f: # this function part will create an empty file in empty.
            pass
        logging.info(f"create file {dir}")
    else :
        logging.info(f"file exist")







    
