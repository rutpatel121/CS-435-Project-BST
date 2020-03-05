import sys
import problem3
import newAVL

layerCt = 0

class Node:

    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

    def insertIter(self, key):
        global layerCt

        currentNode = self
        child = Node(key)
        while True:
            if key <= currentNode.key:
                layerCt += 1
                if currentNode.left is None:
                    currentNode.left = child
                    return
                currentNode = currentNode.left
            else:
                layerCt += 1
                if currentNode.right is None:
                    currentNode.right = child
                    return
                currentNode = currentNode.right

    def deleteRoot(self, node):
        if node == None:
            return None
        if node.left == None:
            return node.right
        if node.right == None:
            return node.left

        nxt = self.findMinIter(node.right)
        nxt.left = node.left
        return node.right

    def deleteIter(self, node, node_delete):
        current = node
        previous = None
        while current != None and current.key != node_delete:
            previous = current
            if node_delete < current.key:
                current = current.left
            elif node_delete > current.key:
                current = current.right

        if previous == None:
            return self.deleteRoot(current)
        if previous.left == current:
            previous.left = self.deleteRoot(current)
        else:
            previous.right = self.deleteRoot(current)

        return node

# print("hi")
    def findMinIter(self, node=None):
        curr = self if node is None else node
        while curr.left is not None:
            curr = curr.left
        return curr
# print("hi")

    def findMaxIter(self, node=None):
        curr = self if node is None else node
        while curr.right is not None:
            curr = curr.right
        return curr
# print("hi")

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

# print("hi")

    def findPrevIter(self, node, key):
        if node is None:
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

# print("hi")


def printInorder(root):
    if root is not None:
        printInorder(root.left)
        print(root.key),
        printInorder(root.right)


def main():
    # root = Node(2)
    # root.insertIter(1)
    # printInorder(root)
    # print("end")
    # root.insertIter(6)
    # printInorder(root)
    # print("added6")
    # root.insertIter(5)
    # printInorder(root)
    # print("added5")
    # root.insertIter(4)
    # printInorder(root)
    # print("added4")
    # root.insertIter(3)
    # printInorder(root)
    # print("added3")
    # root = root.deleteIter(root, 6)
    # printInorder(root)
    # print("deleted6")
    # print('min', root.findMinIter(root).key)
    # print('max', root.findMaxIter(root).key)
    # print('next', root.findNextIter(root, 2).key)
    # print('prev', root.findPrevIter(root, 5).key)

    # problem 5 C / 6 B
    randomArray = problem3.getRandomArray(10000)

    root = Node(randomArray[0])

    for number in randomArray[1:]:
        root.insertIter(number)

    #printInorder(root)
   
    newAVL.root = newAVL.insertIter(None, newAVL.Node(randomArray[0]))
    for number in randomArray[1:]:
        newAVL.insertIter(newAVL.root, newAVL.Node(number))

        
    print('Random')

    print('bst iterative level down: ', layerCt)
    print('avl iterative level down: ', newAVL.layerCt)

    # 6 C
    sortedArr = problem3.getSortedArray(10000)

    root = Node(sortedArr[0])

    for number in sortedArr[1:]:
        root.insertIter(number)

    #printInorder(root)
   
    newAVL.root = newAVL.insertIter(None, newAVL.Node(sortedArr[0]))
    for number in sortedArr[1:]:
        newAVL.insertIter(newAVL.root, newAVL.Node(number))

    print('\nSorted')
    print('bst iterative level down: ', layerCt)
    print('avl iterative level down: ', newAVL.layerCt)

if __name__ == "__main__":
    main()
