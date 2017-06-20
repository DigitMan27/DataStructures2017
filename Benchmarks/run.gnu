set terminal png
set xlabel "NumberOfExecutions"
set ylabel "AverageNumberOfComparisons"
set grid
set output "BenchmarkCharts/Comparisons_Benchmarks/LinearSearch_Comp.png"
plot "LinearSearch_Comp.txt" with lines
set output "BenchmarkCharts/Comparisons_Benchmarks/InterpolationSearch_Comp.png"
plot "InterpolationSearch_Comp.txt" with lines
set output "BenchmarkCharts/Comparisons_Benchmarks/BinarySearch_Comp.png"
plot "BinarySearch_Comp.txt" with lines
set output "BenchmarkCharts/Comparisons_Benchmarks/Comparison_Benchmarks.png"
plot "LinearSearch_Comp.txt" with lines,"InterpolationSearch_Comp.txt" with lines,"BinarySearch_Comp.txt" with lines
set output "BenchmarkCharts/Time_Benchmarks/LinearSearch_Time.png"
plot "LinearSearch_Time.txt" with lines
set output "BenchmarkCharts/Time_Benchmarks/InterpolationSearch_Time.png"
plot "InterpolationSearch_Time.txt" with lines
set output "BenchmarkCharts/Time_Benchmarks/BinarySearch_Time.png"
plot "BinarySearch_Time.txt" with lines
set output "BenchmarkCharts/Time_Benchmarks/TimeBenchmarks.png"
plot "LinearSearch_Time.txt" with lines,"InterpolationSearch_Time.txt" with lines,"BinarySearch_Time.txt" with lines


