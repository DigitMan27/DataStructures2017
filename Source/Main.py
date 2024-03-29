#!/usr/bin/python3


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
              LinearSearch_ID()
            elif SEARCH_CHOICE == 2:
              BinarySearch()
            elif SEARCH_CHOICE == 3:
              pos  = InterpolationSearch()
            elif SEARCH_CHOICE == 4:
                  AVL_Find()
            else:
               print("Invalid Search Option.Please Try Again.")
        elif CHOOSE==5:
             LinearSearch_Name()
        elif CHOOSE==6:
            Exit()
        else:
            print("Invalid Menu Option.Please Try Again.")
       #except ValueError:
        #    print("This is a string.Please try again..")
            


if __name__=="__main__":
   from Operations import *
   from SearchOperations import *
   print(MENU_STR)
   TREE = None #__init__ object value
   SEARCH_CHOICE = -1 #init choice
   while True: 
     try:
      MENU(input("Choice:")) 
     except KeyboardInterrupt:
          print("\nForce Quit..")
          exit(0)
