from setuptools import setup, find_namespace_packages

setup(
    name='microservice', 
    version='1.0',  
    packages=find_namespace_packages(include=['app.*']))