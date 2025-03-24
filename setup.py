# Main purpose: Used by setup tools to define configurations of the project(metadeta, dependencies, etc). Used for packaging and distributing python projects.

from setuptools import find_packages,setup
from typing import List

def get_requirements() -> List[str]:
    '''This function returns the list of the requirements used in the project'''
    requirement_list:List[str] = []

    try:
        with open('requirements.txt', 'r') as file:  #Open and read the requirements.txt file in read mode
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()  #Take out all the empty spaces in the file
                if requirement and requirement != '-e .':  #Skip the line with -e .
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found!")

    return requirement_list
print(get_requirements())

setup(
    name="NetworkSecurity",
    verion='0.0.1',
    author = 'Parth Abhang',
    author_email='parthabhang0124@gmail.com',
    packages=find_packages(),
    install_requirements = get_requirements()
)