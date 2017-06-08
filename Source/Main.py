#!/usr/bin/python

MENU_STR = """
0. Clear CSV File
1. Load Hotels and Reservations from file
2. Save Hotels and Reservations to file
3. Add a Hotel (μαζί και τις κρατήσεις του)
4. Search and Display a Hotel by id{1.Linear/2.Binary/3.InterpolationSearch/4.AVL}
5. Display Reservations by surname search
6. Exit
"""


def MENU(CHOOSE):
    #try:
        CHOOSE = int(CHOOSE)
        if CHOOSE==0:
             Clear()
        elif CHOOSE==1:
             Load()
             LoadResrv()
        elif CHOOSE==2:
             Save()
        elif CHOOSE==3:
             Add()
        elif CHOOSE==4:
            SEARCH_CHOICE = int(input("Choose Search Opt:"))
            if SEARCH_CHOICE == 1:
              print("Lin")
              LinearTimeStart = time.time()
              LinearSearch_ID()
              LineadTimeEnd = time.time()
              print("LinearSearch Executed in:",LineadTimeEnd-LinearTimeStart,"s")
            elif SEARCH_CHOICE == 2:
              print("Bin:")
              BinarySearch()
            elif SEARCH_CHOICE == 3:
              print("Inter:")
              pos  = InterpolationSearch()
            elif SEARCH_CHOICE == 4:
                  AVL_Find()
        elif CHOOSE==5:
             LinearSearch_Name()
             #print("<Not Developed yet>")
        elif CHOOSE==6:
            Exit()
    #except ValueError:
     #      n_error(c)


if __name__=="__main__":
 from Operations import *
 from SearchOperations import *
 print(MENU_STR)
 TREE = None #__init__ object value
 SEARCH_CHOICE = -1
 while True: 
    MENU(input("Choice:"))
