from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    #with open("requirements.txt", "r") as f:
    #    return f.read().splitlines()
    requirement_list :List[str] = []
    return requirement_list

setup(
    name = "sensor",
    version = "1.0.1",
    author="Prajwal Patil",
    author_email="prajwalpatil852@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)