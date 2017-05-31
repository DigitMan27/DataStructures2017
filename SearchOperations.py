#!/usr/bin/python
from Operations import * #import global var + functions
import Operations #import the module as it is and with Operations.<name> put particular variable


#--------------------------------------------------------Search Operations-----------------------------------------------------
def LinearSearch_ID():
        position = 0
        found = False
        L = list(d_H.keys())  #for list be int write list(map(int,d.keys()))
        for i in range(len(L)):
           L[i] = int(L[i])
        print(L)
        ID = input("Put id for searching:")
        while position<len(L) and not found:
             if L[position] == int(ID):
                  found = True
                  #print(found)
                  print(d_H[ID])
             else:
                  position = position +1

def LinearSearch_Name():
      position = 0
      found = False
      N = list(d_R.keys())
      for i in range(len(N)):
         N[i] = str(N[i])
      print(N)
      Name = input("Put name for searching:")
      while position<len(N) and not found:
           if N[position] == str(Name):
              found = True
              print(found)
              print(d_R[str(Name)])
           else:
              position = position + 1


def BinarySearch():
    found = False
    L = list(d_H.keys())
    for i in range(len(L)):
         L[i] = int(L[i])
    L.sort()
    print(L)
    ID = input("Put id for searching:")
    bottom = 0
    top = len(L) + 1
    while not found and bottom <=top:
       middle = (bottom + top)//2
       if L[middle] == int(ID):
          found = True
          #print(found)
          print(d_H[ID])
       elif L[middle] < int(ID):
          bottom = middle + 1
       else:
          top = middle - 1


def InterpolationSearch():
    found = False
    L = list(d_H.keys())
    size  = len(L)
    for i in range(len(L)):
         L[i] = int(L[i])
    L.sort()
    print(L)
    ID = input("Put id for searching:")
    bottom = 0
    middle = -1
    top = int(size - 1)
    while bottom<=top and int(ID)>=L[bottom] and int(ID)<=L[top]:
       if bottom == top | L[bottom] == L[top]:
          print("<Search Failure>")
          exit(1)
       middle = bottom + round(((top-bottom)/(L[top]-L[bottom]))*(int(ID)-L[bottom]))
       if L[middle] < int(ID):
            bottom = middle + 1
       elif L[middle] > int(ID):
            top = middle - 1
       else:
            print("Data is in position:%d"%middle)
            x = L[middle]  
            print(d_H[str(x)])
            return middle
    return -1


#------------------------------AVL_Data_Structure------------------------------
#AVLTree == auto-Balanced BST
#So:
#1.Convert List with IDs in BST
#2.BST Operations(Search,Insert)
#3.BST -> AVLTree    

#+++++++++++++++++++++++++++++++Data_Structure_Operation+++++++++++++++++++++++++++++++
def AVL_Find():
   found = False
   #global tree
   
   ID = int(input("Requested ID:"))
   found = Operations.tree.find(ID)
   print("ID found?(A:",found,")")
   if found:
        print(d_H[str(ID)])
