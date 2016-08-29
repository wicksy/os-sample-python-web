from setuptools import setup, find_packages

setup (
    name             = "pyhelloworld",
    version          = "1.0",
    description      = "Sample Hello World Python application",
    packages         = find_packages(),
    install_requires = ["gunicorn"],
)