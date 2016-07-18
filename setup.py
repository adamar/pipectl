# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

install_requires = [
    'bamboo_api',
]

setup(
    name="cushing",
    version="0.1.0",
    description="A CI/CD Build pipeline DSL",
    license="MIT",
    author="adamar",
    author_email="none@none.com",
    url="http://github.com/adamar/cushing",
    packages=find_packages(),
    install_requires=install_requires,
    scripts=['cushing/cushing'],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ]
)
