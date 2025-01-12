from typing import List
from setuptools import setup, find_packages

HYPEN_E_DOT = "-e ."
def get_requirements(path:str)->List[str]:
    '''
    this function reads the requirements file and returns a list of requirements
    '''
    requiriements = []
    with open(path) as file_obj:
        requiriements = file_obj.readlines()
        requiriements=[req.replace("\n","") for req in requiriements]
        
        if HYPEN_E_DOT in requiriements:
            requiriements.remove(HYPEN_E_DOT)
            
    return requiriements
        

setup(
    name='mlproject',
    version='0.0.1',
    author='Ravina',
    author_email='ravina97more@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)