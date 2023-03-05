from setuptools import setup
from typing import List



# declaring variables for setup functions
PROJECT_NAME = "housing-prediction"
VERSION = "0.0.1"
AUTHOR = "sarfaraz"
DESCRIPTION = "THIS IS MY 1ST PROJECT"
PACKAGES = ["housing"]
REQUIREMENT_FILE_NAME = "requirements.txt"

def get_requirements_list()->list[str]:
    """
    Description: This function is going to return list of requirement
    mention in requirements.txt file

    return this function is going to return a list which contain name
    of libraries mentioned in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()
setup(
name=PROJECT_NAME ,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=PACKAGES,
install_requires = get_requirements_list()

)

