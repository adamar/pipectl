# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

install_requires = [
    'bamboo_api'
    ]

setup(
    name="pipectl",
    version="0.1.1",
    description="A CI/CD Build pipeline DSL",
    license="MIT",
    author="adamar",
    author_email="none@none.com",
    url="http://github.com/adamar/pipectl",
    packages=find_packages(),
    dependency_links=['http://github.com/adamar/python-bamboo-api/tarball/master#egg=bamboo_api'],
    scripts=['pipectl/pipectl'],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ]
)
