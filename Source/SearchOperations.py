#!/usr/bin/python3
from Operations import * #import global var + functions
import Operations #import the module as it is and with Operations.<name> put particular variable


#--------------------------------------------------------Search Operations-----------------------------------------------------
def LinearSearch_ID():
        position = 0
        found = False
        SEARCH_LIST = list(HOTEL_DICT.keys())  #for list be int write list(map(int,d.keys()))
        for i in range(len(SEARCH_LIST)):
           SEARCH_LIST[i] = int(SEARCH_LIST[i])
        ID = input("Put id for searching:")
        while position<len(SEARCH_LIST) and not found:
             if SEARCH_LIST[position] == int(ID):
                  found = True
                  print(HOTEL_DICT[ID])
             else:
                  position = position +1

def LinearSearch_Name():
      position = 0
      found = False
      LINEAR_SEARCH_NAMES_LIST = list(RESERVATIONS_DICT.keys())
      for i in range(len(LINEAR_SEARCH_NAMES_LIST)):
         LINEAR_SEARCH_NAMES_LIST[i] = str(LINEAR_SEARCH_NAMES_LIST[i])
      Name = input("Put name for searching:")
      while position<len(LINEAR_SEARCH_NAMES_LIST) and not found:
           if LINEAR_SEARCH_NAMES_LIST[position] == str(Name):
              found = True
              print(RESERVATIONS_DICT[str(Name)])
           else:
              position = position + 1


def BinarySearch():
    found = False
    SEARCH_LIST = list(HOTEL_DICT.keys())
    for i in range(len(SEARCH_LIST)):
         SEARCH_LIST[i] = int(SEARCH_LIST[i])
    SEARCH_LIST.sort()
    ID = input("Put id for searching:")
    bottom = 0
    top = len(SEARCH_LIST) -1
    while not found and bottom <=top:
       middle = (bottom + top)//2
       if SEARCH_LIST[int(middle)] == int(ID):
          found = True
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
    ID = input("Put id for searching:")
    bottom = 0
    middle = -1
    top = size - 1
    while SEARCH_LIST[bottom] != SEARCH_LIST[top] and int(ID)>=SEARCH_LIST[bottom] and int(ID)<=SEARCH_LIST[top]:
       middle = bottom + round(((top-bottom)/(SEARCH_LIST[top]-SEARCH_LIST[bottom]))*(int(ID)-SEARCH_LIST[bottom]))
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

#+++++++++++++++++++++++++++++++Data_Structure_Operation+++++++++++++++++++++++++++++++
def AVL_Find():
   found = False
   ID = int(input("Requested ID:"))
   found = Operations.TREE.find(ID)
   if found:
        print(HOTEL_DICT[str(ID)])
