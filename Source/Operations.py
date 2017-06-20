#!/usr/bin/python3

#--------Modules--------
import csv
import sys
import time
import os
from sys import platform
from AVL import *

global filename #Name of the csv file

#--------Dictionaries--------
DATA_FULL_DICT = {} #dictionary for all values(Hotels-Reserv)
HOTEL_DICT = {} #dictionary only for Hotels
RESERVATIONS_DICT = {} #dictionary for Reserv

#--------Lists--------
DATA_FULL_LIST = [] 
LINEAR_SEARCH_NAMES_LIST = [] #list for reservations in search operations file
SEARCH_LIST = [] #This list is using in search operations file
RESERVATIONS_LIST = [] #list for reservations names->keys

#--------Variables--------
BLANK = ''
HOTEL_COUNTER = 0 #Initializer for Hotel counter
COLUMN_STEP = 1 #column step for reservations
DEFAULT_FILENAME = os.path.join("../CSVFiles","data.csv") #path for the default csv file
WIN32_DELIMITER = ","
LINUX_DELIMITER = ","
FLAG = False #Is a variable for the program to see if the error function was executed as a result not to show the same message two times
NEWLINE = '\n'

#---------------------------------------File Selector---------------------------------------
if len(sys.argv)<2:
	filename = DEFAULT_FILENAME
else:
	filename = sys.argv[1]

print(filename)


#---------------------------------------Data Cleaner---------------------------------------
def Clear():
     choice = str(input("Clear?(Y/N):"))
     if choice == 'Y'or choice == 'y':
       f = open(filename,'w+')
       f.close()
       print("Success")
     elif choice == 'N'or choice == 'n':
          print("CSV File clear failed")


#---------------------------------------Error Functions---------------------------------------
def fileError(filename):
    print(filename,"Not found")
    
def NumberError(number):
    print("%s is not a number.Please choose an Operation"%number)


#---------------------------------------OPERATIONS---------------------------------------
def Load(): #This Function Loads the Hotel Data
   global HOTEL_COUNTER
   global TREE
   global FLAG
   try:
    if os.stat(filename).st_size == 0:
       print(">CSV File is empty!")
    else:
     with open(filename,'r') as f:
       if platform == "linux":
        reader = csv.reader(f,delimiter = LINUX_DELIMITER)
       elif platform == "win32":
        reader = csv.reader(f,delimiter = WIN32_DELIMITER)
       next(reader)
       TREE = AVLTree() #Create the AVLTree
       for row in reader:
         key = row[0]
         TREE.insert(int(key)) #insert keys as nodes into AVLTree
         if key in DATA_FULL_DICT:
           pass
         DATA_FULL_DICT[key] = row[1:]
         HOTEL_DICT[key] = row[1:4]
         HOTEL_COUNTER = len(DATA_FULL_DICT.keys()) #counts the keys where is inside the dictionary
     f.close()
   except IOError:
       FLAG = True
       fileError()


def LoadResrv(): #This Function Loads the Reservations Data
    global RESERVATIONS_LIST
    global COLUMN_STEP
    try:
     if os.stat(filename).st_size != 0:
      with open(filename,'r') as f:
       if platform == "linux": 
         reader = csv.reader(f,delimiter = LINUX_DELIMITER)
       elif platform == "win32":
         reader = csv.reader(f,delimiter = WIN32_DELIMITER)
       next(reader)
       for row in reader:
         RESERVATIONS_LIST = row[4::3]
         for i in RESERVATIONS_LIST:
             RESERVATIONS_DICT[i] = row[5::COLUMN_STEP]
             if RESERVATIONS_DICT[i] == row[4::3]:
                COLUMN_STEP = COLUMN_STEP + 2
             COLUMN_STEP = COLUMN_STEP + 1
      f.close()
    except IOError:
       if FLAG is not True:
         fileError()


def Add(): #Add Hotels and an number of reserversions to the Hotel
    try:
           global DATA_FULL_LIST
           DATA_FULL_LIST = list(DATA_FULL_DICT)
           del DATA_FULL_LIST[:]
           global HOTEL_COUNTER
           global i_d #ID of the Hotel
           global name #Name of the Hotel
           global stars #Stars of the Hotel
           global Nor #The Number of Rooms(Nor) of the Hotel
           i_d = input("ID:")
           name = input("Name:")
           stars = input("Stars:")
           Nor = input("Num_oF_Rooms:")
           customer_name = input("customer_name:")
           if customer_name is BLANK:
                   return
           checkInDate = input("CheckInDate:")
           DaysToStay = input("DaysToStay:")
           DATA_FULL_LIST.append(i_d)
           DATA_FULL_LIST.append(name)
           DATA_FULL_LIST.append(stars)
           DATA_FULL_LIST.append(Nor)
           DATA_FULL_LIST.append(customer_name)
           DATA_FULL_LIST.append(checkInDate)
           DATA_FULL_LIST.append(DaysToStay)
           HOTEL_COUNTER = len(DATA_FULL_DICT.keys())
           while customer_name is not BLANK:
              customer_name = input("customer_name:")
              if customer_name is BLANK:
                    break
              checkInDate = input("CheckInDate:")
              DaysToStay = input("DaysToStay:")
              DATA_FULL_LIST.append(customer_name)
              DATA_FULL_LIST.append(checkInDate)
              DATA_FULL_LIST.append(DaysToStay)
           DATA_FULL_DICT.update({i_d:name,i_d:stars,i_d:Nor,i_d:DATA_FULL_LIST})
           HOTEL_COUNTER = len(DATA_FULL_DICT.keys())
           with open(filename,'r+',newline='') as f:
               content = f.read()
               f.seek(0,0) #find the first row,column
               f.write(str(HOTEL_COUNTER)) #save there the number of hotels
               f.write(NEWLINE)
           f.close()
           print(DATA_FULL_LIST)
    except ValueError:
         print("Add():<ValueError>")
    except IOError:
         fileError()
         

	
def Save():
    try:
        with open(filename,'a',newline='') as f:
               if platform == "linux":
                 w = csv.writer(f,delimiter=LINUX_DELIMITER,quotechar = '|')
               elif platform == "win32":
                 w = csv.writer(f,delimiter=WIN32_DELIMITER,quotechar = '|')
               w.writerow(DATA_FULL_LIST)
        f.close()
        print("Save Successful...")
        del DATA_FULL_LIST[:]
        DATA_FULL_DICT.clear()
        HOTEL_DICT.clear()
        RESERVATIONS_DICT.clear()
    except IOError:
         print("Save():<IOError>")
         fileError()


def Save_ON_Exit(): #Save before Exit the Program
   try:
    with open(filename,'r+',newline='') as f:
               content = f.read()
               f.seek(0,0)
               f.write(str(HOTEL_COUNTER))
               f.write(NEWLINE)
    f.close()
   except ValueError:
     print("Save_Exit():<ValueError>")
   except IOError:
     print("Save_Exit():<",filename,"not found >")


def Exit():
     Save_ON_Exit()
     print("Saving...")
     print("Quit.")
     del SEARCH_LIST[:]
     del DATA_FULL_LIST[:]
     del RESERVATIONS_LIST[:]
     exit(0)
