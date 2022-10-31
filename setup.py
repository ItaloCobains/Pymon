from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="Pymon",
    version="1.0.0",
    author="ItaloCobains",
    description="Python is a script to start programs whenever they change. Inspired by nodemon.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["Pymon"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Linux",
    ],
    python_requires='>=3.10',
    install_requires=[],
    dependency_links=['https://github.com/ItaloCobains/Pymon']
)