from BenchFunc import *
from CSV_TO_LIST import *

def BinBench():
   key.reverse()
   res = []
   pop = 0
   avg = 0.0
   s = 0
   end = 0
   times = 0
   f = open("Bbench.txt","w")
   #f1 = open("time.txt","w")
   while(times<1000):
       pop = BinarySearch(key)
       res.append(pop) 
       avg = sum(res)/(len(key)-1)
       f.write(str(times)+" "+str(avg)+"\n")
    #f1.write(str(times)+" "+str(end)+"\n")
       times = times+1
       #avg =  0
    #s = 0
    #end = 0
   del res[:]
   f.close()
   #f1.close()
Load()
BinBench()
