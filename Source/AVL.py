#!/usr/bin/python3

#-------------------------------------------AVLTree Implementation in Python-------------------------------------------

#AVLNode -> Is the class for the nodes which apart the whole AVLTree
class AVLNode(object):
   def __init__(self,data): #The constructor
       self.data = data #data of the node
       self.right_child = None #right child of the node
       self.left_child = None #left child of the node
       self.parent = None #parent of node
       self.height = 0 #the height of the node
       self.balance = 0 #The balance of the node
       
   def update_height(self,upwards = True):
       if self.left_child is None: #If the node has not a left child then
          left_height = 0
       else: 
          left_height = self.left_child.height + 1  #increase the height of the node plus 1  
       if self.right_child is None:  #If the node has not a right child then
          right_height = 0   
       else:
          right_height = self.right_child.height + 1 #increase the height of the node plus 1
       self.balance = left_height-right_height    #diff the left and right height to find the balance
       height = max(left_height,right_height)    #the Height is the max of the two heigths
       if self.height !=height:  
          self.height = height
          if self.parent is not None: #If the node has not parent and upwards is true then call the update_heigth for the parent
             if upwards:
                self.parent.update_height()   
   
   def is_left(self):
       if self.parent is None:  #If the node has no parent
          return self.parent    #return the parent of the node
       else:
          return self is self.parent.left_child   #return the left child of the parent of the node


#AVL Tree->Is the class for the AVL Tree data structure 
class AVLTree(object):
    
   def __init__(self): #Constructor
       self.root = None  #root of the node
   
   def right_rotation(self,root):  #rotate to the right the subtree
       left = root.is_left()   #left is root's parent left child or the parent itself
       pivot = root.left_child  
       if pivot is None:
          return
       root.left_child = pivot.right_child  #the right child is in pos of the left child
       if pivot.right_child is not None: #if root's left child of right child exist 
          root.left_child.parent = root  #The parent of the right child of the root is equal with root
       pivot.right_child = root
       pivot.parent = root.parent
       root.parent = pivot
       if left is None: 
          self.root = pivot
       elif left:
          pivot.parent.left_child = pivot
       else:
          pivot.parent.right_child = pivot
       root.update_height(False)
       pivot.update_height(False)

   def left_rotation(self,root):
       left = root.is_left()  #left is root's parent left child or the parent itself
       pivot = root.right_child
       if pivot is None:
          return
       root.right_child = pivot.left_child #the left child is in pos of the right child
       if pivot.left_child is not None:  #if root's right child of left child exist 
          root.right_child.parent = root  #The parent of the right child of the root is equal with root
       pivot.left_child = root
       pivot.parent = root.parent
       root.parent = pivot
       if left is None:
          self.root = pivot
       elif left:
          pivot.parent.left_child = pivot
       else:
          pivot.parent.right_child = pivot
       root.update_height(False) #root update height but not upwards
       pivot.update_height(False) #pivot update height but not upwards


   def balance(self,node): #this method checks the balance of the tree (must : |balance|=<1)
       node.update_height(False)
       if node.balance == 2:
          if node.left_child.balance !=-1:  #if the balance of the left child of the node is not equal to -1 then
             self.right_rotation(node)  #do right rotation 
             if node.parent.parent is not None: 
                self.balance(node.parent.parent)  #call recursively the balance method
          else:
              self.left_rotation(node.left_child)
              self.balance(node)
       elif node.balance == -2:
            if node.right_child.balance != 1:
               self.left_rotation(node)
               if node.parent.parent is not None:
                  self.balance(node.parent.parent)
            else:
                self.right_rotation(node.right_child)
                self.balance(node)
       else:
            if node.parent is not None:
               self.balance(node.parent)

   def insert(self,data,node = None):
       if node is None: # if there is no node
          node = self.root # node is root
          if node is None:  #if there is not root
             node = AVLNode(data=data) # a node created from above class 
             self.root = node #root is equal the that node
             return node # returns the node
          else:
               ret = self.insert(data=data,node=node)
               self.balance(ret)
               return ret
       if node.data == data:
          return node
       elif node.data > data:  
               child = node.left_child
               if child is None:
                  child = AVLNode(data=data)
                  child.parent = node
                  node.left_child = child
                  node.update_height()
                  return child
               else:
                   return self.insert(data=data,node = child)
       elif node.data < data:
               child = node.right_child
               if child is None: 
                  child = AVLNode(data=data)
                  child.parent = node
                  node.right_child = child
                  node.update_height()
                  return child
               else:
                   return self.insert(data=data,node = child)
       else:
              print(".../ERROR/...")


   def find(self,data,node = None):
       found = False
       if node is None:
          node = self.root
          if self.root is None:
             return None
          else:
             return self.find(data,self.root)
       elif node.data == data:
            found = True
            return found
       elif data < node.data:
            if node.left_child is None:
               return found 
            else:
                return self.find(data,node.left_child)
       else:
            if node.right_child is None:
                return found
            else:
                return self.find(data,node.right_child)
