"""Stores application installation information"""

from setuptools import setup, find_packages


def requirements():
    with open("requirements.txt", 'r') as require:
        return require.read()


with open("README.md", 'r') as readme:
    long_description = readme.read()

setup(
    name='department_app',
    version='0,1',
    description='This package include department application',
    author='Aliaksei Strunets',
    install_requires=requirements(),
    packages=find_packages(),
)
