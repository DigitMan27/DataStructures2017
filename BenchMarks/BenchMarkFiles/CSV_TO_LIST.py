#bin/usr/python3
import csv

key = []

def Load():
    global key
    with open("Samples/data1.csv") as f:
      reader = csv.reader(f,delimiter = ';')
      #next(reader)
      for row in reader:
         key.append(int(row[0]))

