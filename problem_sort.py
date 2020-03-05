import sys

class Node:
  def __init__(self, key):
    self.left = None
    self.right = None
    self.key = key
  
  def insertRec(self, key):
    child = Node(key)
    if key >= self.key:
      if self.right is None:
        self.right = child
      else:
        self.right.insertRec(key)
    else:
      if self.left is None:
        self.left = child
      else:
        self.left.insertRec(key)

def helper(node, array):
  if node == None:
    return None
  helper(node.left, array)
  array.append(node.key)
  helper(node.right, array)

def sort(array):
  if len(array) == 0:
      return None
  root = Node(array[0])
  for values in array[1:]:
    root.insertRec(values)
  sortedArray = list()
  helper(root, sortedArray)
  return sortedArray

def printInorder(root):  
    if root is not None:
        printInorder(root.left) 
        print(root.key), 
        printInorder(root.right)

def main():
    
  array = [1, 12, 9, 7, 5]
  sortedArray = sort(array)
  for values in sortedArray:
    print(values)
  pass
 
if __name__ == "__main__":
  main()    