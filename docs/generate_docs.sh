#!/bin/bash

cd ~/plotly-graph
sudo python3 setup.py install
sphinx-apidoc -f -o docs/source igviz/
cd docs
make html
sudo pip3 uninstall igviz -y
