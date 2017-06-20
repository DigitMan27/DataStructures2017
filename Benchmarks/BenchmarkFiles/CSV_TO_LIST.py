#bin/usr/python3
import csv

key = []

def Load():
    global key
    with open("Samples/data.csv") as f:
      reader = csv.reader(f,delimiter = ';')
      for row in reader:
         key.append(int(row[0]))

