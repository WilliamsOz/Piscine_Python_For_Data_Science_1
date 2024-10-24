"""
name:
    Will be used to install the package.
version:
    A string that uniquely identifies the version of the package.
description:
    This description will be displayed when the user installs the package.
author:
    Name of the person or organization that created the package.
author_email:
    The author's email address.
url:
    URL where the user can find more information about the package.
packages:
    Tells the setuptools module where to find the Python modules that
    are included in the package.
classifiers:
    A list of keywords that are used to categorize the package.
    These keywords are used by package managers to find packages that
    are relevant to the user's needs.
entry_points:
    A list of console scripts for the package.
    These scripts can be run from the command line.
"""
from setuptools import setup, find_packages


setup(
    name='ft_package',
    version='0.0.1',
    description='A sample test package',
    author='wiozsert',
    author_email='wiozsert@student.42.fr',
    home_page='https://github.com/WilliamsOz/Piscine_python/\
        /c00/ex09/ft_package',
    packages=find_packages(),
    license='MIT',
    location="/home/wiozsert/...",
    requires="",
    requires_by="",
    metadata_version="2.1",
    installers="pip",
    classifiers=[],
    entry_points={},
)
