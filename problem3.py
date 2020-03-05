import random

def getRandomArray(n):
    a = set()
    returnlst = []    
    while(len(a) != n):
        number = random.randrange(1, n + 1)
        if number not in a:
            a.add(number)
            returnlst.append(number)
    return returnlst

def getSortedArray(n):
  returnlst = []
  for i in range(n, 0, -1):
    returnlst.append(i)
  return returnlst

# print('sorted:',getSortedArray(10))
# print('random:',getRandomArray(10))


