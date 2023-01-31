'''
def test_range(n):
  if n in range(3,9):
    result = f"{n} is in the range"
  else:
    result = "not in range"
  return result

print(test_range(int(input("enter number: "))))  
'''

'''def up(string):
  string = input("enter string: ")
  return 
  '''














'''main = []
even = []
odd = []
d = []

def myfunc(*numbers):
  for i in range(1,16):
    numbers = int(input("enter number: "))
    main.append(numbers)
    if numbers % 2==0:
      even.append(numbers)
    if numbers % 2!=0:
      odd.append(numbers)   
  for j in main:
    if main.count(j) > 1:
      d.append(j)
  return (d,main,even,odd)


myfunc()
print(main)
print(even)
print(odd)
'''

main = []
even = []
odd = []
duplicate = []

def myfunc(*num):

  for i in range(15):
    num = int(input("enter number: "))
    if num in main:
      duplicate.append(num)
    else:
      if num%2==0:
        even.append(num)
      else:
        odd.append(num)
      
      main.append(num)
  return (main,even,odd,duplicate)


print(myfunc())