#!/bin/python

class BST:
   def __init__(self,data):
       self.left = None
       self.right = None
       self.data = data

   def insert(self,data):
       if self.data:
          if data < self.data:
             if self.left is None:
                self.left = BST(data)
             else:
                self.left.insert(data)
          elif data > self.data:
             if self.right is None:
                self.right = BST(data)
             else:
                self.right.insert(data)
       else:
           self.data = data
   

   def find(self,data,parent=None):
       found = False
       if data < self.data:
          if self.left is None:
             return found
             #return None,None
          return self.left.find(data,self)
       elif data > self.data:
           if self.right is None:
              #found = False
              return found
              #return None,None
           return self.right.find(data,self)
       else:
           found = True
           return found
           #return self,parent,found



   def Print_Tree(self): 
       if self.left:
          self.left.Print_Tree()
       print(self.data)
       if self.right:
          self.right.Print_Tree()   
                

d = {1:"popa",22:"oplk",3:"ewq"}
l = list(d.keys())
l.sort()
root = BST(l[0])
for item in l:
    root.insert(item)
ID = int(input("ID for searching:"))
found = root.find(ID)
#print(found)
if found:
   print(d[ID])
else:
   print("Not found")
#print(node,parent)
root.Print_Tree()
