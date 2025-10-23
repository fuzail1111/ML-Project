from setuptools import setup, find_packages
from typing import List
def get_requirements(file_path: str) -> List[str]:
    with open(file_path, 'r') as file:
        requirements = file.readlines()
    return [req.strip() for req in requirements if req.strip() and not req.startswith('#')]
setup(
    name='mlproject',
    version='0.0.1',
    author='Fuzail',
    author_email='chudgarfuzail684@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
