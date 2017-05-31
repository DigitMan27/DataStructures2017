#Copyright (c) 2017 Konstantinos Adamopoulos All Rights Reserved.
#!/usr/bin/python
import csv
import sys
import time
from AVL import *

intro = """
0. Clear CSV File
1. Load Hotels and Reservations from file
2. Save Hotels and Reservations to file
3. Add a Hotel (μαζί και τις κρατήσεις του)
4. Search and Display a Hotel by id{1.Linear/2.Binary/3.InterpolationSearch/4.AVL}
5. Display Reservations by surname search
6. Exit
"""

F = []
A = []
L = []
d = {} #dictionary for all values(Hotels-Reserv)
d_H = {} #dictionary only for Hotels
d_R = {} #dictionary for Reserv
Res = [] #list for reservations names->keys
blank = ''

counter = 0
c = 1
global filename
tree = None #__init__ object value


#File Selector
if len(sys.argv)<2:
	filename = "data.csv"
else:
	filename = sys.argv[1]

print(filename)


#Clear the csv file
def Clear():
     ch = str(input("Clear?(Y/N):"))
     if ch == 'Y'or ch=='y':
       f = open(filename,'w+')
       f.close()
       print("Success")
     elif ch=='N'or ch=='n':
          print("CSV File clear failed")


#Error Functions:
def error():
    print("csv file not found")
    
def n_error(w):
    print("%s is not a number.Please choose an Operation"%w)


#-----------------OPERATIONS------------------
def Load(): #This Function Loads the Hotel Data
   global counter
   global i
   global tree
   try:
     with open(filename,'r') as f:
       reader = csv.reader(f,delimiter = ';')
       next(reader)
       tree = AVLTree() #Create the AVLTree
       for row in reader:
         key = row[0]
         tree.insert(int(key)) #insert keys as nodes into AVLTree
         if key in d:
           pass
         d[key] = row[1:]
         d_H[key] = row[1:4]
         #d_R[key_r] = row[6:8]
         counter = len(d.keys()) #counts the keys where is inside the dictionary
   except IOError:
     error()


def LoadResrv(): #This Function Loads the Reservations Data
    global Res
    global c
    try:
     with open(filename,'r') as f:
       reader = csv.reader(f,delimiter = ';')
       next(reader)
       for row in reader:
         Res = row[4::3]
         for i in Res:
             d_R[i] = row[5::c]
             if d_R[i] == row[4::3]:
                c = c +2
             c =c +1
         #print(d_R)
         #print(list(d_R.keys()))
         #print(d_R) 
    except IOError:
        error()


def Add(): #Add Hotels and an number of reserversions to the Hotel
    try:
           global F
           F = list(d)
           del F[:]
           global counter
           global i_d
           global name
           global stars
           global Nor
           i_d = input("ID:")
           name = input("Name:")
           stars = input("Stars:")
           Nor = input("Num_oF_Rooms:")
           customer_name = input("customer_name:")
           if customer_name is blank:
                    exit(1)
           checkInDate = input("CheckInDate:")
           DaysToStay = input("DaysToStay:")
           F.append(i_d)
           F.append(name)
           F.append(stars)
           F.append(Nor)
           F.append(customer_name)
           F.append(checkInDate)
           F.append(DaysToStay)
           print(F)
           #d.update({id:name,id:stars,id:Nor,id:customer_name,id:checkInDate,id:DaysToStay})
           counter = len(d.keys())
           while customer_name is not blank:
              customer_name = input("customer_name:")
              if customer_name is blank:
                    break
              checkInDate = input("CheckInDate:")
              DaysToStay = input("DaysToStay:")
              F.append(customer_name)
              F.append(checkInDate)
              F.append(DaysToStay)
           d.update({i_d:name,i_d:stars,i_d:Nor,i_d:F})
           print(F)
           print(d)
           counter = len(d.keys())
           with open(filename,'r+',newline='') as f:
               content = f.read()
               f.seek(0,0) #find the first row,column
               f.write(str(counter)) #save there the number of hotels
               f.write("\n")
           f.close()
           print(F)
    except ValueError:
         print("Add():<ValueError>")

	
def Save():
    try:
        with open(filename,'a',newline='') as f:
               w = csv.writer(f,delimiter=';',quotechar = '|')
               #d = [i_d,';',name,';',stars,';',Nor,';']
               w.writerow(F)
        f.close()
        del F[:]
        d.clear()
    except IOError:
         print("Save():<IOError>")


def Save_Exit(): #Save before Exit the Program
   try:
    with open(filename,'r+',newline='') as f:
               content = f.read()
               f.seek(0,0)
               f.write(str(counter))
               f.write("\n")
    f.close()
   except ValueError:
     print("Save_Exit():<ValueError>")


def Exit():
     Save_Exit()
     print("Saving...")
     print("Quit")
     del L[:]
     del F[:]
     del A[:]
     del Res[:]
     #d.clear()
     exit(1)

'''
#-------------------Search Operations-------------------
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
   global tree
   ID = int(input("Requested ID:"))
   found = tree.find(ID)
   print("ID found?(A:",found,")")
   if found:
        print(d_H[str(ID)])
       
'''   
    
'''
#----------------------------------Main+Menu-----------------------------------
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


#Main:
print(intro)
search_choice = 0
while 1: 
    Menu(input("Choice:"))
    


'''
