#!/bin/python
'''
AVLTree Implementation in Python
'''
#AVLNode -> Is the class for the nodes which apart the whole AVLTree
class AVLNode(object):
   def __init__(self,data):
       self.data = data
       self.right_child = None
       self.left_child = None
       self.parent = None
       self.height = 0
       self.balance = 0
       
   def update_height(self,upwards = True):
       if self.left_child is None:
          left_height = 0
       else:
          left_height = self.left_child.height + 1
       if self.right_child is None:
          right_height = 0
       else:
          right_height = self.right_child.height + 1
       self.balance = left_height-right_height
       height = max(left_height,right_height)
       if self.height !=height:
          self.height = height
          if self.parent is not None:
             if upwards:
                self.parent.update_height()
   
   def is_left(self):
       if self.parent is None:
          return self.parent
       else:
          return self is self.parent.left_child



class AVLTree(object):
    
   def __init__(self):
       self.root = None
   
   def right_rotation(self,root):
       left = root.is_left()
       pivot = root.left_child
       if pivot is None:
          return
       root.left_child = pivot.right_child
       if pivot.right_child is not None: 
          root.left_child.parent = root
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
       left = root.is_left()
       pivot = root.right_child
       if pivot is None:
          return
       root.right_child = pivot.left_child
       if pivot.left_child is not None:
          root.right_child.parent = root
       pivot.left_child = root
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


   def balance(self,node):
       node.update_height(False)
       if node.balance == 2:
          if node.left_child.balance !=-1:
             self.right_rotation(node)
             if node.parent.parent is not None:
                self.balance(node.parent.parent)
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
       if node is None:
          node = self.root
          if node is None:
             node = AVLNode(data=data)
             self.root = node
             return node
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
                  node.update_height() #my edit of code
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
            #return node
       elif data < node.data:
            if node.left_child is None:
               return found
               #return node 
            else:
                return self.find(data,node.left_child)
       else:
            if node.right_child is None:
                return found
                #return node
            else:
                return self.find(data,node.right_child)

'''     
   def plot(self,balance=False):
       #import igraph as igraphs
       G = igraphs.Graph()
       if self.root is not None:
          G.add_vertices(1)
       queue = [[self.root,0]]
       index = 0
       not_break = True
       while(not_break):
            node = queue[0][0]
            node_index = queue[0][1]
            if not balance:
               G.vs[node_index]['label'] = node.data
            else:
               G.vs[node_index]['label'] = node.balance
            if index == 0:
               G.vs[node_index]['pos'] = 'root'
            if node.left_child is not None:
               G.add_vertices(1)
               G.add_edges([(node_index,index+1)])
               queue.append([node.left_child,index+1])
               G.vs[index+1]['pos'] = 'lch'
               index +=1
            if node.right_child is not None:
               G.add_vertices(1)
               G.add_edges([(node_index, index+1)])
               G.vs[index+1]['pos']='rch'
               queue.append([node.right_child, index+1])
               index += 1

            queue.pop(0)
            if len(queue)==0:
               not_break = False
       layout = G.layout_reingold_tilford(root=0)
       igraphs.plot(G,layout=layout)  
'''

'''
#------------------------------------/Example/------------------------------------
l = [1,2,3,4,5,67,77,100,200,440,2121,2111,21245,2111,11,22]
l.sort()
B = AVLTree()
for item in l:
    B.insert(item)
   # B.plot(True)

ID = int(input("ID for searching:"))
found = B.find(ID)
#print(found)
if found:
   print(found)
   #print(d[ID])
else:
   print("Not found")

'''













