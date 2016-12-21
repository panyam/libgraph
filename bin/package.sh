#!/bin/sh

rm -Rf build dist libgraph.egg-info
python setup.py sdist
python setup.py bdist_wheel --universal
rm -Rf libgraph.egg-info
