#!/bin/python3
import time
import numpy as np
import random

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
    for i in range(len(L)):
         L[i] = int(L[i])
    L.sort()
    ID = random.randint(min(L),max(L))
    bottom = 0
    count = 0
    top = len(L) -1
    while not found and bottom <=top:
       count = count + 1
       middle = bottom + (top-bottom)//2
       if L[int(middle)] == int(ID):
          found = True
          return count
          #count = count + 1
       elif L[int(middle)] < int(ID):
          bottom = middle + 1
       else:
          top = middle - 1
    return count

def InterpolationSearch(L):
    found = False
    #SEARCH_LIST = list(HOTEL_DICT.keys())
    size  = len(L)
    for i in range(len(L)):
         L[i] = int(L[i])
    L.sort()
    ID = random.randint(min(L),max(L))
    bottom = 0
    middle = -1
    top = size - 1
    count = 0
    while L[bottom] != L[top] and int(ID)>=L[bottom] and int(ID)<=L[top]:
       count = count + 1
       middle = bottom + round(((top-bottom)/(L[top]-L[bottom]))*(int(ID)-L[bottom]))
       if L[middle] < int(ID):
            bottom = middle + 1
       elif L[middle] > int(ID):
            top = middle - 1
       else:
            #print("Data is in position:%d"%middle)
            x = L[middle]  
            #print(HOTEL_DICT[str(x)])
            return middle
    if int(ID) == L[bottom]:
       #print("Data is in position:%d"%bottom)
       return bottom
    else:
      return -1
    return count

def Listing(N):
    L = []
    for i in range(N):
        L.append(random.randint(N,2*N))
    return L

P = []
P = Listing(1500) #number of ids

