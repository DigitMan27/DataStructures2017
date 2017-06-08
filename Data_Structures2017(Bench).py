#!/bin/python
import time
import numpy as np
import random
import cProfile
import re
import timeit
from timeit import Timer

def LinearSearch(L):
        position = 0
        count = 0
        found = False
        for i in range(len(L)):
           L[i] = int(L[i])
        #print(L)
        ID = random.randint(min(L),max(L))
        #print(ID)
#        start = time.time()
        while position<len(L) and not found:
             count = count +1
             if L[position] == int(ID):
                  found = True
                  #print(found)
                  #print(d_H[ID])
             else:
                  position = position +1
 #       end = time.time()-start
        return count

def BinarySearch(L):
    found = False
    count = 0
    for i in range(len(L)):
         L[i] = int(L[i])
    L.sort()
    A1 = np.array(L)
    #print(L)
    ID = random.randint(min(A1),max(A1))
    #print(ID)
    bottom = 0
    top = len(A1) + 1
    #start = time.time()
    while not found and bottom <=top:
       middle = (bottom + top)//2
       count = count + 1
       if A1[middle] == int(ID):
          found = True
          #print(found)
          #print(d_H[ID])
       elif A1[middle] < int(ID):
          bottom = middle + 1
       else:
          top = middle - 1
    #end = time.time() - start
    return count
    #del L[:]

'''
def isSorted(ary):
    for i in range(len(ary)):
        if ary[i] < ary[i - 1]:
            return False
    return True

'''

def InterpolationSearch(L):
    found = False
    size  = len(L)
    for i in range(len(L)):
         L[i] = int(L[i])
    L.sort()
    ID = random.randint(min(L),max(L))
    bottom = 0
    middle = -1
    count=0
    top = int(size - 1)
    #start = time.time()
    while int(bottom)<=int(top) and int(ID)>=L[int(bottom)] and int(ID)<=L[int(top)]:
       #count = count + 1
       if int(bottom) == int(top) | L[int(bottom)] == L[int(top)]:
          print("<Search Failure>")
          exit(1)
       middle = bottom + round(((top-bottom)/(L[top]-L[bottom]))*(int(ID)-L[bottom]))
       #print(middle)
       if L[int(middle)] < int(ID):
            bottom = middle + 1
       elif L[int(middle)] > int(ID):
            top = middle - 1
       else:
            #count = count +1
            #print("Data is in position:%d"%middle)
            x = L[int(middle)]  
            #print(d_H[str(x)])
            return middle
    return -1
    #end = time.time()-start
    #return end

def binarySearch (arr, l, r, x):
 
    # Check base case
    if r >= l:
 
        mid = l + (r - l)/2
 
        # If element is present at the middle itself
        if arr[int(mid)] == x:
            return mid
         
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[int(mid)] > x:
            return binarySearch(arr, l, mid-1, x)
 
        # Else the element can only be present in right subarray
        else:
            return binarySearch(arr, mid+1, r, x)
 
    else:
        # Element is not present in the array
        return -1



def Listing(N):
    L = []
    for i in range(N):
        L.append(random.randint(0,2*N))
    return L

P = []
A = []
def menu():
   P = Listing(1000)
   P.reverse()
   res = []
   pop = 0
   avg = 0.0
   s = 0
   end = 0
   times = 0
   f = open("bench.txt","w")
   f1 = open("time.txt","w")
   while(times<10):
    #s = time.time()
    for i in range(1000):
       #for j in range()
       #start = time.time()
       #pop = LinearSearch(P)
       #end = time.time() - s
       pop = BinarySearch(P)
       res.append(pop)
       #res = res  + binSearch(P,random.randint(100,1000),0,len(P)-1)
       #BinarySearch(P)
       #InterpolationSearch(P)
       #binarySearch(P,0,len(P)-1,random.randint(0,10000))
       #end = time.time()
       #res = end - start
    #end = time.time() - s 
    avg = sum(res)/(len(P))
    f.write(str(times)+" "+str(avg)+"\n")
    #f1.write(str(times)+" "+str(end)+"\n")
    times = times+1
    avg =  0
    #s = 0
    #end = 0
    del res[:]
   f.close()
   f1.close()
   #del P[:]


menu()



