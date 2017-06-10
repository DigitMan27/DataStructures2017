#!/bin/bash

CSVfilePath=../CSVFiles/$2
if [ "$1" == "-h" ]
then
  echo "None option -> Default File"
  echo "If \$1=1 -> file from CSVFIles path"
  echo "If \$1=2 -> file from other path"
elif [ -z "$1" ] && [ -z "$2" ]
then
  clear
  echo "None Option"
  echo ">Welcome To the Execution Program"
  echo ">Execute..."
  python3 ../Source/Main.py  #Default csv file
  rm -rf ../Source/__pycache__
  echo ">Thank You"
elif [ "$1" -eq "1" ]
then
  clear
  echo "OPTION $1"
  echo ">Welcome To the Execution Program"
  echo ">Execute..."
  python3 ../Source/Main.py ${CSVfilePath}  #User csv file
  rm -rf ../Source/__pycache__
  echo ">Thank You"
elif [ "$1" -eq "2" ]
then
  clear
  echo "OPTION $1"
  echo ">Welcome To the Execution Program"
  echo ">Execute..."
  python3 ../Source/Main.py $2  #csv file from another path
  rm -rf ../Source/__pycache__
  echo ">Thank You"
else
  echo ">ERROR!!"
fi
