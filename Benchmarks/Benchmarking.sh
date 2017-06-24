#!/bin/bash

PathToFile=BenchmarkFiles

File1=BinarySearch_Comp.txt
File2=InterpolationSearch_Comp.txt
File3=LinearSearch_Comp.txt
File4=LinearSearch_Time.txt
File5=InterpolationSearch_Time.txt
File6=BinarySearch_Time.txt

clear
echo "======LinearSearch======"
echo "python3 ${PathToFile}/LinearSearch_Bench.py"
python3 ${PathToFile}/LinearSearch_Bench.py
echo "======BinarySearch======"
echo "python3 ${PathToFile}/BinarySearch_Bench.py"
python3 ${PathToFile}/BinarySearch_Bench.py
echo "======InterpolationSearch======"
echo "python3 ${PathToFile}/InterpolationSearch_Bench.py"
python3 ${PathToFile}/InterpolationSearch_Bench.py

rm -rf ${PathToFile}/__pycache__
printf "\n"
echo ">Plotting in BenchmarkCharts Folder with GNUPLOT."
gnuplot run.gnu
rm  $File1
rm  $File2
rm  $File3
rm  $File4
rm  $File5
rm  $File6
echo ">The Benchmark Is Finished."
echo ">Thank You."
