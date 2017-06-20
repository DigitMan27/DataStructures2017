from SearchFunctions import *
from CSV_TO_LIST import *

import time

def InterBench():
   key.reverse()
   res = []
   pop = 0
   avg = 0.0
   start = 0
   end = 0
   times = 0
   f = open("InterpolationSearch_Comp.txt","w")
   f0 = open("InterpolationSearch_Time.txt","w")
   while(times<1000):
       start = time.time()
       pop = InterpolationSearch(key)
       end += time.time() - start
       res.append(pop)
       avg = sum(res)/(len(key)-1)
       f.write(str(times)+" "+str(avg)+"\n")
       f0.write(str(times)+" "+str(end)+"\n")
       times = times+1
       start = 0
   del res[:]
   f.close()
   f0.close()

Load()
InterBench()
