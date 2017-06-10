set terminal png
set xlabel "NumberOfExecutions"
set ylabel "AverageNumberOfComparisons"
set grid
set output "BenchMarkCharts/LinearBench.png"
plot "Lbench.txt" with lines
set output "BenchMarkCharts/InterBench.png"
plot "Ibench.txt" with lines
set output "BenchMarkCharts/BinBench.png"
plot "Bbench.txt" with lines
set output "BenchMarkCharts/BenchMarks.png"
plot "Lbench.txt" with lines,"Ibench.txt" with lines,"Bbench.txt" with lines
