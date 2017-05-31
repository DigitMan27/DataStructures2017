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


def Menu(c):
    #try:
        c = int(c)
        if c==0:
             Clear()
        elif c==1:
             Load()
             LoadResrv()
        elif c==2:
             Save()
        elif c==3:
             Add()
        elif c==4:
            search_choice = int(input("Choose Search Opt:"))
            if search_choice == 1:
              print("Lin")
              LinearTimeStart = time.time()
              LinearSearch_ID()
              LineadTimeEnd = time.time()
              print("LinearSearch Executed in:",LineadTimeEnd-LinearTimeStart,"s")
            elif search_choice == 2:
              print("Bin:")
              BinarySearch()
            elif search_choice == 3:
              print("Inter:")
              pos  = InterpolationSearch()
            elif search_choice == 4:
                  AVL_Find()
        elif c==5:
             LinearSearch_Name()
             #print("<Not Developed yet>")
        elif c==6:
            Exit()
    #except ValueError:
     #      n_error(c)


if __name__=="__main__":
 from Operations import *
 from SearchOperations import *
 print(MENU_STR)
 tree = None #__init__ object value
 search_choice = 0
 while 1: 
    Menu(input("Choice:"))
