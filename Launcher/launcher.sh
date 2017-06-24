#!/bin/bash

CSVfilePath=../CSVFiles/$2
if [ "$1" == "-h" ]
then
  echo "None Option:Default File(CSVFiles/data.csv)"
  echo "If \$1=1:File From CSVFiles Folder \$2=<Filename>.csv"
  echo "If \$1=2:File From Other Path \$2=Path"
elif [ -z "$1" ] && [ -z "$2" ]
then
  clear
  echo "None Option"
  echo ">Welcome.."
  echo ">Execute..."
  python3 ../Source/Main.py  #Default csv file
  rm -rf ../Source/__pycache__
  echo ">Thank You"
elif [ "$1" -eq "1" ]
then
  clear
  echo "OPTION $1"
  echo ">Welcome.."
  echo ">Execute..."
  python3 ../Source/Main.py ${CSVfilePath}  #User csv file
  rm -rf ../Source/__pycache__
  echo ">Thank You"
elif [ "$1" -eq "2" ]
then
  clear
  echo "OPTION $1"
  echo ">Welcome.."
  echo ">Execute..."
  python3 ../Source/Main.py $2  #csv file from another path
  rm -rf ../Source/__pycache__
  echo ">Thank You"
else
  echo ">ERROR!!"
fi
