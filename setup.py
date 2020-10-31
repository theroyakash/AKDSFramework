from setuptools import setup, find_packages
from os import path

__version__ = '1.0.0'

here = path.abspath(path.dirname(__file__))

setup(
    name='AKDSFramework',
    version=__version__,
    description='Python Package for all your data structure and algorithm needs',
    url='https://github.com/theroyakash/akdsframework',
    download_url='https://github.com/theroyakash/akdsframework/tarball/main',
    license='MIT License',
    packages=find_packages(),
    include_package_data=True,
    author='theroyakash',
    author_email='royakashappleid@icloud.com'
)
