#!/bin/python3
import random

def LinearSearch(L):
        position = 0
        count = 0
        found = False
        for i in range(len(L)):
           L[i] = int(L[i])
        ID = random.randint(min(L),max(L))
        while position<len(L) and not found:
             count = count +1
             if L[position] == int(ID):
                  found = True
             else:
                  position = position +1
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
       elif L[int(middle)] < int(ID):
          bottom = middle + 1
       else:
          top = middle - 1
    return count

def InterpolationSearch(L):
    found = False
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
            x = L[middle]  
            return middle
    if int(ID) == L[bottom]:
       return bottom
    else:
      return -1
    return count

