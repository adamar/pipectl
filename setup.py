# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name="pipectl",
    version="0.1.7",
    description="A CI/CD Build pipeline DSL",
    license="MIT",
    author="adamar",
    author_email="none@none.com",
    url="http://github.com/adamar/pipectl",
    packages=find_packages(),
    install_requires=[
        "bamboo_api",
        "GitPython>=2.0.0"
        ],
    dependency_links=[
        'git://github.com/adamar/python-bamboo-api.git#egg=bamboo_api'
        ],
    scripts=['pipectl/pipectl'],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ]
)
