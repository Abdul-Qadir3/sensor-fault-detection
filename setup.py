# from setuptools import find_packages ,setup
# # from typing import list

# def get_requirements()->list[str]:
    
#     req_list = list[str] = []

#     return req_list





# setup(
# name= 'sensor',
# version= '0.0.1',
# author= 'Abdul Qadir',
# author_email= 'aq452831@gmail.com',
# packages= find_packages(),
# # install_requires=['pymongo'] #avoiding list for package installation
# install_requires=get_requirements() #function calling

# )







from setuptools import find_packages, setup

def get_requirements() -> list[str]:
    req_list: list[str] = []
    return req_list

setup(
    name='sensor',
    version='0.0.1',
    author='Abdul Qadir',
    author_email='aq452831@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)
