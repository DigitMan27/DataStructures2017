#!/bin/bash

CSVfile=$1
echo ">Welcome To the Execution Program"
echo ">Execute..."
python3 Main.py ${CSVfile}
rm -rf __pycache__
echo ">Thank You"
