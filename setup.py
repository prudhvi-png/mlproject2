from setuptools import setup, find_packages
from typing import List


HIGHFEN_E_DOT = '-e .'
def get_requirements(requirements):
    

    '''This function will return the list requirements'''
    
    with open("requirements.txt", "r") as file_obj:
        
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

    if HIGHFEN_E_DOT in requirements:
        requirements.remove(HIGHFEN_E_DOT)

    return requirements
        

setup(
    name= "Second Ml-Project",
    version= "0.0.1" ,
    author= "Prudhvi Ganesh",
    author_email= "prudhviredrouth143@gmail.com",
    packages= find_packages(),
    install_requires = get_requirements(requirements="requirements.txt")

)

