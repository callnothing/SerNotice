# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os

setup(
    name="ServerNotice",
    version="0.01",
    description="easy to notify administrator by server",
    author="Alan Wang",
    author_email="wangchengchao115@gmail.com",
    license="GPL",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'snotice = snotice.__main__:main',
        ]
    },
)
