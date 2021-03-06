from setuptools import setup, find_packages

setup(
    name="regcore",
    version="2.0.0",
    license="public domain",
    packages=find_packages(),
    install_requires=[
        'django>=1.8,<1.9',
        'django-mptt',
        'jsonschema',
        'six',
    ]
)
