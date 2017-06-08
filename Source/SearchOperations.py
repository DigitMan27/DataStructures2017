#!/usr/bin/python
from Operations import * #import global var + functions
import Operations #import the module as it is and with Operations.<name> put particular variable


#--------------------------------------------------------Search Operations-----------------------------------------------------
def LinearSearch_ID():
        position = 0
        found = False
        SEARCH_LIST = list(HOTEL_DICT.keys())  #for list be int write list(map(int,d.keys()))
        for i in range(len(SEARCH_LIST)):
           SEARCH_LIST[i] = int(SEARCH_LIST[i])
        print(SEARCH_LIST)
        ID = input("Put id for searching:")
        while position<len(SEARCH_LIST) and not found:
             if SEARCH_LIST[position] == int(ID):
                  found = True
                  #print(found)
                  print(HOTEL_DICT[ID])
             else:
                  position = position +1

def LinearSearch_Name():
      position = 0
      found = False
      LINEAR_SEARCH_NAMES_LIST = list(RESERVATIONS_DICT.keys())
      for i in range(len(LINEAR_SEARCH_NAMES_LIST)):
         LINEAR_SEARCH_NAMES_LIST[i] = str(LINEAR_SEARCH_NAMES_LIST[i])
      print(LINEAR_SEARCH_NAMES_LIST)
      Name = input("Put name for searching:")
      while position<len(LINEAR_SEARCH_NAMES_LIST) and not found:
           if LINEAR_SEARCH_NAMES_LIST[position] == str(Name):
              found = True
              print(found)
              print(RESERVATIONS_DICT[str(Name)])
           else:
              position = position + 1


def BinarySearch():
    found = False
    SEARCH_LIST = list(HOTEL_DICT.keys())
    for i in range(len(SEARCH_LIST)):
         SEARCH_LIST[i] = int(SEARCH_LIST[i])
    SEARCH_LIST.sort()
    print(SEARCH_LIST)
    ID = input("Put id for searching:")
    bottom = 0
    top = len(SEARCH_LIST) #+ 1
    while not found and bottom <=top:
       middle = (bottom + top)//2
       if SEARCH_LIST[int(middle)] == int(ID):
          found = True
          #print(found)
          print(HOTEL_DICT[ID])
       elif SEARCH_LIST[int(middle)] < int(ID):
          bottom = middle + 1
       else:
          top = middle - 1


def InterpolationSearch():
    found = False
    SEARCH_LIST = list(HOTEL_DICT.keys())
    size  = len(SEARCH_LIST)
    for i in range(len(SEARCH_LIST)):
         SEARCH_LIST[i] = int(SEARCH_LIST[i])
    SEARCH_LIST.sort()
    print(SEARCH_LIST)
    ID = input("Put id for searching:")
    bottom = 0
    middle = -1
    top = size - 1
    while SEARCH_LIST[bottom] != SEARCH_LIST[top] and int(ID)>=SEARCH_LIST[bottom] and int(ID)<=SEARCH_LIST[top]:
       #if bottom == top | SEARCH_LIST[bottom] == SEARCH_LIST[top]:
        #  print("<Search Failure>")
         # exit(1)
       middle = bottom + round(((top-bottom)/(SEARCH_LIST[top]-SEARCH_LIST[bottom]))*(int(ID)-SEARCH_LIST[bottom]))
       #mid = low + ((iD-L[low])*(high-low)//(L[high]-L[low]))
       if SEARCH_LIST[middle] < int(ID):
            bottom = middle + 1
       elif SEARCH_LIST[middle] > int(ID):
            top = middle - 1
       else:
            print("Data is in position:%d"%middle)
            x = SEARCH_LIST[middle]  
            print(HOTEL_DICT[str(x)])
            return middle
    if int(ID) == SEARCH_LIST[bottom]:
       print("Data is in position:%d"%bottom)
       return bottom
    else:
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
   ID = int(input("Requested ID:"))
   found = Operations.TREE.find(ID)
   print("ID found?(A:",found,")")
   if found:
        print(HOTEL_DICT[str(ID)])