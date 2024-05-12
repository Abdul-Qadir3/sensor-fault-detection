# Importing necessary functions from setuptools package
# find_packages will go and search for the pakages . it will consider a folder as pakage as it sees __init__.py
from setuptools import find_packages, setup

# Function to retrieve project dependencies
def get_requirements() -> list[str]:
    # Initialize an empty list to store requirements
    req_list: list[str] = []
    # Return the list of requirements
    return req_list

# Configuration of the project setup
setup(
    # Name of the project
    name='sensor',

    # Version of the project
    version='0.0.1',

    # Author of the project
    author='Abdul Qadir',

    # Email address of the project author
    author_email='aq452831@gmail.com',

    # Automatically find all packages and sub-packages in the project
    packages=find_packages(),

    # Retrieve project dependencies using the get_requirements function
    install_requires=get_requirements()
)
