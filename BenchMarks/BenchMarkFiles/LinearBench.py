from BenchFunc import *
from CSV_TO_LIST import *

def LinBench():
   key.reverse()
   res = []
   pop = 0
   avg = 0.0
   s = 0
   end = 0
   times = 0
   f = open("Lbench.txt","w")
   #f1 = open("time.txt","w")
   while(times<1000):
    #s = time.time()
    #for i in range(1000):
       #for j in range()
       #start = time.time()
       pop = LinearSearch(key)
       #end = time.time() - s
       #pop = BinarySearch(P)
       res.append(round(pop))
       #res = res  + binSearch(P,random.randint(100,1000),0,len(P)-1)
       #BinarySearch(P)
       #InterpolationSearch(P)
       #binarySearch(P,0,len(P)-1,random.randint(0,10000))
       #end = time.time()
       #res = end - start
    #end = time.time() - s 
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
   #del P[:]
Load()
LinBench()
