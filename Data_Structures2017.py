#!/usr/bin/python
import csv
import sys

intro = """
0.Clear CSV File
1. Load Hotels and Reservations from file
2. Save Hotels and Reservations to file
3. Add a Hotel (μαζί και τις κρατήσεις του)
4. Search and Display a Hotel by id{1.Linear/2.Binary/3.InterpolationSearch}
5. Display Reservations by surname search
6. Exit
"""

F = []
A = []
L = []
d = {} #dictionary for all values(Hotels-Reserv)
d_H = {} #dictionary only for Hotels
blank = ''

counter = 0
global filename


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


#OPERATIONS
def Load():
   global counter
   try:
     with open(filename,'r') as f:
       reader = csv.reader(f,delimiter = ';')
       next(reader)
       for row in reader:
         key = row[0]
         if key in d:
           pass
         d[key] = row[1:]
         d_H[key] = row[1:4]
         counter = len(d.keys())
   except IOError:
     error() 	 

def Add():
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
               f.seek(0,0)
               f.write(str(counter))
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


def Save_Exit():
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
     print("Saving...Thank you for using my program Have a Nice Day!!")
     del L[:]
     del A[:]
     #d.clear()
     exit(1)

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

'''
def LinearSearch_Name():
      position = 0
      found = False
      N = list(d.values())
      print(N)
      Name = input("Put name for searching:")
      while position<len(L) and not found:
           if N[position] == Name:
              found = True
              print(found)
              print(d[Name])
           else:
              position = position + 1
'''
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

#-----------------Main+Menu------------------
def Menu(c):
    #try:
        c = int(c)
        if c==0:
             Clear()
        elif c==1:
             Load()
        elif c==2:
             Save()
        elif c==3:
             Add()
        elif c==4:
            search_choice = int(input("Choose Search Opt:"))
            if search_choice == 1:
              print("Lin")
              LinearSearch_ID()
            elif search_choice == 2:
              print("Bin:")
              BinarySearch()
            elif search_choice == 3:
              print("Inter:")
              pos  = InterpolationSearch()
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
    



