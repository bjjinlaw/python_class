'''
a = []
def newlist(*num):
  for i in range(5):
    l1 = int(input("enter number: "))
    a.append(l1)
'''
'''
  size = len(a)
  temp = a[0]
  a[0] = a[size-1]
  a[size-1]=temp
  
  return a

print(newlist())
'''

'''
new = []
def newlist(*list1):
  for i in range(5):
    list1 = int(input("enter number: "))
    new.append(list1)
  new[0],new[-1]=new[-1],new[0]
  return new

print(newlist())
'''
'''
new = []

def newlist(*list1):
  for i in range(5):
    list1 = int(input("enter number: "))
    new.append(list1)
  get = new[0], new[-1]
  new[-1],new[0] = get
  return new

print(newlist()) 

'''

'''
def newlist(num):
  [start, *middle, end] = num
  num = [end, *middle, start]
  return num

print(newlist([1,2,3,4,5]))  
'''

'''
def newlist(num):
  first = num.pop(0)
  last = num.pop(-1)
  
  num.insert(0, last)
  num.insert(-1, first)
  
  return num

print(newlist([1,2,3,4,5]))
'''

'''
def swapPositions(list, pos1, pos2):
     
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list
 
# Driver function
List = [23, 65, 19, 90]
pos1, pos2  = 1, 3
 
print(swapPositions(List, pos1-1, pos2-1))
'''

