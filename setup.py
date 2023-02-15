#!/usr/bin/env python
import os

from pkg_resources import parse_requirements
from setuptools import find_packages, setup

_PATH_ROOT = os.path.dirname(__file__)


def _load_requirements(path_dir: str = _PATH_ROOT, file_name: str = "requirements.txt") -> list:
    reqs = parse_requirements(open(os.path.join(path_dir, file_name)).readlines())
    return list(map(str, reqs))


setup(
    name="lit_label_studio",
    version="0.0.1",
    description="label studio",
    author="Robert S Lee",
    author_email="sangkyulee@gmail.com",
    url="https://github.com/Lightning-AI/lit_label_studio",
    install_requires=_load_requirements(),
    packages=find_packages(),
    include_package_data=True,
    package_data={"": ["nginx-8080.conf"]},
)
