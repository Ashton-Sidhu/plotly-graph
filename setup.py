from setuptools import find_packages, setup
from setuptools.command.install import install

VERSION = "0.3.1"

pkgs = [
    "networkx==2.4",
    "plotly==4.5.2",
]

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="igviz",
    url="https://github.com/Ashton-Sidhu/plotly-graph",
    packages=find_packages(),
    author="Ashton Sidhu",
    author_email="ashton.sidhu1994@gmail.com",
    install_requires=pkgs,
    version=VERSION,
    license="MIT",
    description="A library to plot Graphs with Plotly.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="datascience, machinelearning, visualization, graph",
    python_requires=">= 3.6",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Development Status :: 4 - Beta",
    ],
)
