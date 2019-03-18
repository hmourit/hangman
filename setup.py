# This Python file uses the following encoding: utf-8

from setuptools import find_packages
from setuptools import setup

setup(
    name='hangman',
    version='0.1',
    packages=find_packages(),
    url='https://github.com/hmourit/hangman',
    author='hmourit',
    author_email='hmourit@gmail.com',
    description='Hangman game package',
    entry_points={
        'console_scripts': ['hangman=hangman.cli:main']
    }
)
