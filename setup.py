import os
import re
import sys

from setuptools import setup, find_packages

setup(
    name='dlclouds',
    version='1.0.0.dev1',
    packages=find_packages(exclude=['build*','contrib', 'docs', 'tests*']),
    package_dir={'': './'},
    entry_points={
        'console_scripts': [
            'dlclouds=dlclouds.cli:handle',
            # 'dlc=dlclouds.cli:handle',
        ]
    },
    url='dlclouds.com',
    license='MIT',
    author='Constantine G.',
    author_email='constantine.gurnov@gmail.com',
    description=''
)
