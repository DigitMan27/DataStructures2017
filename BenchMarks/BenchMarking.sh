#!/bin/bash

PathToFile=BenchMarkFiles
File1=Bbench.txt
File2=Ibench.txt
File3=Lbench.txt

clear
echo "======LinearSearch======"
echo "python3 ${PathToFile}/LinearBench.py"
python3 ${PathToFile}/LinearBench.py
echo "======BinarySearch======"
echo "python3 ${PathToFile}/BinBench.py"
python3 ${PathToFile}/BinBench.py
echo "======InterpolationSearch======"
echo "python3 ${PathToFile}/InterBench.py"
python3 ${PathToFile}/InterBench.py

rm -rf ${PathToFile}/__pycache__
printf "\n"
echo ">Plotting in BenchMarkCharts Folder with GNUPLOT."
gnuplot run.gnu
rm  $File1
rm  $File2
rm  $File3
echo ">Benchmarking Is Finished."
echo ">Thank You."
