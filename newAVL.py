import random

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

# node to null
root = None
layerCt = 0

def balance_factor(node):
    left_h = 0
    right_h = 0

    if node:
        if node.left:
            left_h = node.left.height
    if node:
        if node.right:
            right_h = node.right.height
    return left_h - right_h

def isBalanced(node):
    if node:
        return abs(balance_factor(node)) <= 1
    return 1

def height_Calculation(node):

    left_h = 0
    right_h = 0

    if node:
        if node.left:
            left_h = node.left.height
    if node:
        if node.right:
            right_h = node.right.height

    return max(left_h, right_h) + 1

def leftRotate(node):

    temp = node.right
    node.right = temp.left
    temp.left = node
    node.height = height_Calculation(node)
    temp.height = height_Calculation(temp)

    return temp

def rightRotate(node):

    temp = node.left
    node.left = temp.right
    temp.right = node
    node.height = height_Calculation(node)
    temp.height = height_Calculation(temp)

    return temp

def balance(node):

    difference = balance_factor(node)

    if difference > 1:
        l_balance = balance_factor(node.left)

        if l_balance < 0:
            node.left = leftRotate(node.left) 

        node = rightRotate(node)
        return node
    else:
        r_balance = balance_factor(node.right)
        if r_balance > 0:
            node.right = rightRotate(node.right)
        node = leftRotate(node)
    return node

def insertIter(node, key):

    global layerCt
    if node == None:
        return key

    current = node
    parent = None
    insertkey = key.key
    stack = []
    track = []

    # going left or right
    while current is not None:
        layerCt += 1
        currkey = current.key
        parent = current
        stack.append(parent)
        if insertkey < currkey:
            current = current.left
            track.append('0')
        else:
            track.append('1')
            current = current.right
 
    if insertkey < parent.key:
        parent.left = key
    else:
        parent.right = key

    global root
    track.pop()
    previous = None
    for i in range(len(stack)):
        node = stack[-i-1]
        if i != 0:
            if len(track) > 0 and track.pop() == '0':
                node.left = previous
            else:
                node.right = previous
        
        node = node if isBalanced(node) else balance(node)

        previous = node
        node.height = height_Calculation(node)
    
    root = previous

def helper(curr):
    global root
    parent = root
    temp = root.left

    # finding next max element's parent node
    while temp.right:
        parent = temp
        temp = temp.right

    curr.key = temp.key

    if temp.left:
        if temp.left.key < parent.key:
            parent.left = temp.left
        elif temp.left.key > parent.key:
            parent.right = temp.left

    # if there's no right node
    else:
        if temp.key < parent.key:
            parent.left = None
        else:
            parent.right = None

def deleteIter(curr, node_delete):
    global root
    parent = None
    
    if curr != None:

        # if node is to be deleted
        if curr.key == node_delete.key:
            
            if curr.left != None and curr.right != None:
                helper(curr)
                if isBalanced(curr) == False:
                    root = balance(curr)
                    return
            
            # if there is a right child and no left child go right
            elif curr.left == None and curr.right != None:
                root = curr.right
            
            # if there is a left child and no right child go left
            elif curr.left != None and curr.right == None:
                root = curr.left

            # checking left and right nodes if they are empty, it will return None because tree is empty
            elif curr.left == None and curr.right == None:
                root = None
            
            if isBalanced(curr) == False:
                root = balance(curr)
                root.height = height_Calculation(root)
            
            return

        stack = []
        track = []
        temp = curr
        # if node is not a node, we delete
        while temp != None and temp.key != node_delete.key:
            parent = temp
            stack.append(parent)

            if node_delete.key > temp.key:
                temp = temp.right
                track.append('1')
            
            elif node_delete.key < temp.key:
                temp = temp.left
                track.append('0')

        if temp.left != None and temp.right != None:
            helper(temp)
            if isBalanced(curr) == False:
                root = balance(curr)
                root.height = height_Calculation(root)
                return

        # if right node exists but no left node
        elif temp.left == None and temp.right != None:
            if node_delete.key < parent.key:
                parent.left = temp.right
            else:
                parent.right = temp.right

        # if left node exists but no right node
        elif temp.left != None and temp.right == None:
            if node_delete.key < parent.key:
                parent.left = temp.left
            else:
                parent.right = temp.left

        elif temp.left == None and temp.right == None:
            if node_delete.key < parent.key:
                parent.left = None
            else:
                parent.right = None

        track.pop()
        previous = None

        for i in range(len(stack)):   
            node = stack[- i - 1]
            # print("node: ", node.key)
            if i != 0:
                if len(track) > 0 and track.pop() == '0':
                    node.left = previous
                else:
                    node.right = previous
            node = node if isBalanced(node) else balance(node)
            previous = node
            node.height = height_Calculation(node)

        return
    
    return

def findMinIter(node):
    if node == None:
        return node
    temp = node
    while temp.left:
        temp = temp.left
    return temp.key

def findMaxIter(node):
    if node == None:
        return node
    temp = node
    while temp.right:
        temp = temp.right
    return temp.key

def findPrevIter(self, node, key):
    if node == None:
        return node
    temp = node
    checker = None
    previousNode = None
    
    while temp != key and temp.key != key:

        if key > temp.key:
            temp = temp.right
        elif key < temp.key:
            previousNode = temp
            temp = temp.left
        if temp and temp.left:
            checker = temp.left
        while checker.right:
            checker = checker.right
        return checker
    return previousNode

def findNextIter(self, node, key):
    temp = node

    while temp != key and temp.key != key:
        if key > temp.key:
            temp = temp.right
        elif key < temp.key:
            temp = temp.left
    checker = None

    if temp.right:
        checker = temp.right
        while checker.left:
            checker = checker.left
        return checker

    while node:
        if temp.key < node.key:
            checker = node
            node = node.left
            continue
        elif temp.key > node.key:
            node = node.right
        else:
            break

    return checker

def printInorder(root):  
    if root:
      printInorder(root.left)
      print(root.key, end=' ')
      printInorder(root.right)



# root = insertIter(root, Node(5))
# printInorder(root)
# print()
# insertIter(root, Node(8))
# printInorder(root)
# print('added 8')
# print()

# insertIter(root, Node(4))
# printInorder(root)
# print('added 4')
# print()

# insertIter(root, Node(3))
# printInorder(root)
# print('added 3')
# print()

# insertIter(root, Node(9))
# printInorder(root)
# print('added 9')
# print()

# insertIter(root, Node(0))
# printInorder(root)
# print('added 0')
# print()

# insertIter(root, Node(1))
# printInorder(root)
# print('added 1')
# print()

# deleteIter(root, Node(4))
# printInorder(root)
# print('deleted 4')
# print()

# """
# arr = getRandomArray(10000)
# root = Node(arr[0])
# for i in range(1, len(arr), 1):
#     root = insertIter(root, arr[i])

# _root = Node(arr[0])
# for i in range(1, len(arr), 1):
#     insertIter(_root, arr[i])
# """