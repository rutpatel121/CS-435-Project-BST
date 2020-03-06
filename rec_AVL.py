class TreeNode(object): 

    def __init__(self, key): 
        self.key = key 
        self.left = None
        self.right = None
        self.height = 1
  
    def insert(self, root, key): 

        if not root: 
            return TreeNode(key) 
        elif key < root.key: 
            root.left = self.insert(root.left, key) 
        else: 
            root.right = self.insert(root.right, key) 

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right)) 
  
        balance = self.getBalance(root) 
  
        #If the node is unbalanced,   
        if balance > 1 and key < root.left.key: 
            return self.rightRotate(root) 
  
        #Right Right 
        if balance < -1 and key > root.right.key: 
            return self.leftRotate(root) 
  
        #Left Right 
        if balance > 1 and key > root.left.key: 
            root.left = self.leftRotate(root.left) 
            return self.rightRotate(root) 
  
        #Right Left 
        if balance < -1 and key < root.right.key: 
            root.right = self.rightRotate(root.right) 
            return self.leftRotate(root) 
  
        return root 
  
    def delete(self, root, key): 
  
        # Step 1 - Perform standard BST delete 
        if not root: 
            return root 
  
        elif key < root.key: 
            root.left = self.delete(root.left, key) 
  
        elif key > root.key: 
            root.right = self.delete(root.right, key) 
  
        else: 
            if root.left is None: 
                temp = root.right 
                root = None
                return temp 
  
            elif root.right is None: 
                temp = root.left 
                root = None
                return temp 
  
            temp = self.getMinValueNode(root.right) 
            root.key = temp.key 
            root.right = self.delete(root.right, 
                                      temp.key) 
  
        # If the tree has only one node, return it 

        if root is None: 
            return root 
  
        #Update the height
         
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right)) 
  
        #Get the balance factor 
        balance = self.getBalance(root) 
  
        # If the node is unbalanced then Left Left
        if balance > 1 and self.getBalance(root.left) >= 0: 
            return self.rightRotate(root) 
  
        # Right Right 
        if balance < -1 and self.getBalance(root.right) <= 0: 
            return self.leftRotate(root) 
  
        # Left Right 
        if balance > 1 and self.getBalance(root.left) < 0: 
            root.left = self.leftRotate(root.left) 
            return self.rightRotate(root) 
  
        # Right Left 
        if balance < -1 and self.getBalance(root.right) > 0: 
            root.right = self.rightRotate(root.right) 
            return self.leftRotate(root) 
  
        return root 
  
    def leftRotate(self, turn): 
  
        r = turn.right 
        rot = r.left 
  
        #rotation 
        r.left = turn 
        turn.right = rot 
  
        # Update heights 
        turn.height = 1 + max(self.getHeight(turn.left), self.getHeight(turn.right)) 
        r.height = 1 + max(self.getHeight(r.left), self.getHeight(r.right)) 

        # Return the new root 
        return r 
  
    def rightRotate(self, turn): 
  
        r = turn.left 
        route = r.right 
  
        # Perform rotation 
        r.right = turn 
        turn.left = route 
  
        # Update heights 
        turn.height = 1 + max(self.getHeight(turn.left), self.getHeight(turn.right)) 
        r.height = 1 + max(self.getHeight(r.left), self.getHeight(r.right)) 
  
        # Return the new root 
        return r 
  
    def getHeight(self, root): 
        if not root: 
            return 0
  
        return root.height 
  
    def getBalance(self, root): 
        if not root: 
            return 0
  
        return self.getHeight(root.left) - self.getHeight(root.right) 
  
    def getMinValueNode(self, root): 
        if root is None or root.left is None:
            return root 
        # temp = root
        # while temp.left:
        #     temp = temp.left
        # return temp
        return self.getMinValueNode(root.left)

    def getMaxValueNode(self, root):
        if root is None or root.right is None:
            return root
        return self.getMaxValueNode(root.right) 
  
    def inOrder(self, root): 
  
        if not root: 
            return
        
        self.inOrder(root.left) 
        print("{0} ".format(root.key), end="") 
        
        self.inOrder(root.right) 
  
    def findNext(self, root, next, num):
        if root == None:
            next = None
            # print("findNext root None")
            return next
        
        if (root.key == num):
            if (root.right):
                # print("findnext right currnode: ", root.key)
                #print(self.getMinValueNode(root.right).key)
                next = self.getMinValueNode(root.right)
                # print("root right next.key ", next.key)
                # return next.key
                
        elif (num < root.key):
            next = root
            next = self.findNext(root.left, next, num)

        else:
            next = self.findNext(root.right, next, num)
        
        return next

    def findPrev(self, root, num):
        inorder = []
        def _inOrder(root):
            if root is None:
                return
            
            _inOrder(root.left)
            inorder.append(root.key)
            _inOrder(root.right)

        _inOrder(root)
        # print("prev: ", inorder)
        if num not in inorder:
            return None
        
        idx = inorder.index(num) - 1
        if idx >= 0:
            return inorder[idx]


myTree = TreeNode(21) 
root = None
#nums = [9, 5, 10, 0, 6, 11, -1, 1, 2] 
  
#for num in nums: 
root = myTree.insert(root, 9)
root = myTree.insert(root, 5)
root = myTree.insert(root, 10)
root = myTree.insert(root, 1)
root = myTree.insert(root, 4)
root = myTree.insert(root, 2) 
  
# Preorder Traversal 
print("After insertion") 
myTree.inOrder(root) 
print()
print('min', myTree.getMinValueNode(root.left.right).key)
print('max', myTree.getMaxValueNode(root).key)
print('root', root.key)
print('next', myTree.findNext(root, None, 4).key)
print('prev', myTree.findPrev(root ,2 ))
# Delete 
key = 10
root = myTree.delete(root, key) 
  
print("After deletion") 
myTree.inOrder(root) 
print() 