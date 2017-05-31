#Copyright (c) 2017 Konstantinos Adamopoulos All Rights Reserved.
#!/usr/bin/python3
import csv
import sys
import time
from sys import platform
from AVL import *


F = []
A = []
L = []
d = {} #dictionary for all values(Hotels-Reserv)
d_H = {} #dictionary only for Hotels
d_R = {} #dictionary for Reserv
Res = [] #list for reservations names->keys
blank = ''

counter = 0 #Initializer for Hotel counter
c = 1
global filename #Name of the csv file
DEFAULT_FILENAME = "data.csv"
WIN32_DELIMITER = ","
LINUX_DELIMITER = ";"
Flag = False #Is a variable for the program to see if the error function was executed as a result not to show the same message two times


#File Selector
if len(sys.argv)<2:
	filename = DEFAULT_FILENAME
else:
	filename = sys.argv[1]

print(filename)


#------------------------Data Cleaner---------------------
def Clear():
     ch = str(input("Clear?(Y/N):"))
     if ch == 'Y'or ch=='y':
       f = open(filename,'w+')
       f.close()
       print("Success")
     elif ch=='N'or ch=='n':
          print("CSV File clear failed")


#---------------------Error Functions-------------------
def error():
    print("csv file not found")
    
def n_error(w):
    print("%s is not a number.Please choose an Operation"%w)


#---------------------OPERATIONS-----------------------
def Load(): #This Function Loads the Hotel Data
   global counter
   global i
   global tree
   global Flag
   try:
     with open(filename,'r') as f:
       if platform == "linux":
        reader = csv.reader(f,delimiter = LINUX_DELIMITER)
       elif platform == "win32":
        reader = csv.reader(f,delimiter = WIN32_DELIMITER)
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
       Flag = True
       error()


def LoadResrv(): #This Function Loads the Reservations Data
    global Res
    global c
    try:
     with open(filename,'r') as f:
       if platform == "linux": 
         reader = csv.reader(f,delimiter = LINUX_DELIMITER)
       elif platform == "win32":
         reader = csv.reader(f,delimiter = WIN32_DELIMITER)
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
       if Flag is not True:
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
               if platform == "linux":
                 w = csv.writer(f,delimiter=LINUX_DELIMITER,quotechar = '|')
               elif platform == "win32":
                 w = csv.writer(f,delimiter=WIN32_DELIMITER,quotechar = '|')
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
   except IOError:
     print("Save_Exit():<",filename,"not found >")


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
