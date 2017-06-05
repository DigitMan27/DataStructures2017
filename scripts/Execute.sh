#!/bin/bash

CSVfilePath=../CSVFiles/$2
if [ -z "$1" ] && [ -z "$2" ]
then
  clear
  echo "None Option"
  echo ">Welcome To the Execution Program"
  echo ">Execute..."
  python3 ../source/Main.py  #Default csv file
  rm -rf ../source/__pycache__
  echo ">Thank You"
elif [ "$1" -eq "1" ]
then
  clear
  echo "OPTION $1"
  echo ">Welcome To the Execution Program"
  echo ">Execute..."
  python3 ../source/Main.py ${CSVfilePath}  #User csv file
  rm -rf ../source/__pycache__
  echo ">Thank You"
elif [ "$1" -eq "2" ]
then
  clear
  echo "OPTION $1"
  echo ">Welcome To the Execution Program"
  echo ">Execute..."
  python3 ../source/Main.py $2  #csv file from another path
  rm -rf ../source/__pycache__
  echo ">Thank You"
else
  echo ">ERROR!!"
fi
