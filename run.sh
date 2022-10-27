#!/bin/bash

python plotter.py

pycodestyle $(git ls-files "*.py")

cd test/unit
python test_processor.py

cd ../func
bash test_plotter.sh

