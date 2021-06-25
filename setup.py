# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages
import os

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()


def read_requirements():
    """Parse requirements from requirements.txt."""
    reqs_path = os.path.join('.', 'requirements.txt')
    with open(reqs_path, 'r') as f:
        requirements = [line.rstrip() for line in f]
    return requirements


setup(
    name='lazmond3-pylib-twitter',
    version='0.0.6',
    description='twitter cli 0.0.6: text and rename,  0.0.5: user profile 0.0.4: video thum mp4 bitrate,  0.0.3: video_thum, 0.0.2: video_url',
    long_description=readme,
    author='lazmond3',
    author_email='moikilo00@gmail.com',
    url='https://github.com/lazmond3/pylib-twitter.git',
    install_requires=["requests", "lazmond3-pylib-debug"],
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    test_suite='tests'
)
