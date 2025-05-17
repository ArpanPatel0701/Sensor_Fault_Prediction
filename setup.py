from setuptools import find_packages, setup
from typing import List


# HYPEN_E_DOT='-e .'


# def get_requirements(file_path:str)->list[str]:
#     requirements = []
#     with open(file_path) as file_obj:
#         requirements=file_obj.readlines()
#         requirements=[req.replace("\n","") for req in requirements]


#         if HYPEN_E_DOT in requirements:
#             requirements.remove(HYPEN_E_DOT)


#     return requirements


def get_requirements()->list[str]:
    requirements_list : List[str] = []
    return requirements_list



setup(
    name="sensor",
    version="0.0.1",
    author="Arpan Patel",
    author_email="arpanpatel0701@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()   # first use  :   install_requires = get_requirements('requirements.txt)

)





