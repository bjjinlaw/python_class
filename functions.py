'''def greet():
  print("hello")
  print("welcome")

greet()
'''
'''def greet(fname,lname):
  print(f"hello {fname},{lname}")
  print("welcome")

greet("bijay","magar")
'''
'''def add(a,b):
  return a + b
result = add(a=1,b=2)
print(result)
'''
'''def add(a,b=2):
  return a + b
print(add(1,4))
print(add(1))'''

def multiply(*numbers):
  total = 1
  for num in numbers:
    total = total*num
  return total

print(multiply(1,2,3,4,5))


