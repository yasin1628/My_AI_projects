import os
from pathlib import Path 
import logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'Text_Summarizer'
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/conponents/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",

]

for file_path in list_of_files:
    file_path = Path(file_path)
    file_dir, file = os.path.split(file_path)
    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Created directory {file_dir} for file {file_path}")
    if (not os.path.exists(file_path)) or (os.path.getsize(file)) == 0:
        logging.info(f"Creating file {file_path}")
        with open(file, 'w') as f:
            pass    
    else:
        logging.info(f"File {file_path} already exists")