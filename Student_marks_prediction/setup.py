from setuptools import find_packages,setup
from typing import List

bachslash_n = "-e ."
def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as path_obj:
        requirements = path_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if bachslash_n in requirements:
            requirements.remove(bachslash_n)
    return requirements

setup(
    name = "Heart_Disease_Prediction",
    version = '0.0.1',
    author="Yaseen Ahmad",
    author_email="ahmadyaseen1628@gmail.com",
    install_requires = get_requirements('requirements.txt'),
    packages=find_packages()
)