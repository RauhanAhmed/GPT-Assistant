from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."
def get_requirements(path : str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(path) as obj:
        requirements = obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        requirements.remove(HYPEN_E_DOT)

        return requirements

setup(
    name = "gpt_assistant",
    version = "0.0.1",
    author = "Rauhan Ahmed",
    author_email = "rauhaan.siddiqui@gmail.com",
    license = "MIT",
    packages = find_packages(),
    install_requires = get_requirements("requirements.txt")
)