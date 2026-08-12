'''
this setup.py file is an essential part of packaging and distributing Python projects. 
It contains metadata about the project, such as its name, version, author, and dependencies. 
The setup.py file is used by tools like setuptools to build and install the package.
'''

from setuptools import setup, find_packages,Setup
from typing import List

def get_requirements() -> List[str]:
    """
    This function reads the requirements.txt file and returns a list of dependencies.
    """
    try:
        with open('requirements.txt') as file:
            #Read lines from the file
            lines=file.readlines()
            ## Process each line
            for line in lines:
                requirement=line.strip()
                ## ignore empty lines and -e.
                
