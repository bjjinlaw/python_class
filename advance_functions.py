'''def greet():
  print("Hello Students!")
  print("Good Morning.")
  
g = greet
g()
'''

#def addition(num1, num2):
#  print(num1,num2)

#a = addition
#a(10,15)

#def outer():
  #print("I am outer function")
#  def inner():
#    print("I am inner function")
#  inner()
#outer()

'''def calculator():
  def addition(num1,num2):
    print(num1+num2)
  return addition

add = calculator()
add(10,15)
'''

'''def calculator(operator):
  def addition(a,b):
    return a+b
  def difference(a,b):
    return a-b
  def product(a,b):
    return a*b
  if operator == "+":
    return addition
  if operator == "-":
    return difference
  if operator == "*":
    return product

a = calculator(input("operator"))
print(a(int(input("num1")), int(input("num2"))))
'''

# closure
'''
def increment(num):
  def factor(val):
    return num + val
  return factor

increase_by = increment(20)
print(increase_by(10))
print(increase_by(30))

'''

'''def greater(x,y):
  if x>y:
    return x
  return y
def greater3(x,y,z):
  return greater(x, greater(y,z))
print(greater3(1,3,2))
'''
 
'''def welcome(name):
  print(f"Welcome {name}")
  
def bye_bye(name):
  print(f"Bye Bye {name}") 
  
def greet(func):
  func("Ram")
  
greet(bye_bye)
'''

'''def decorate_function(func):
  def wrapper():
    print("Hello Everyone!")
    func()
    print("Bye Everyone!")
  return wrapper

@decorate_function
def welcome():
  print("welcome Everyone")
  
#w = decorate_function(welcome)
#w()
welcome()
'''
'''
def smart_division(func):
  def wrapper(a,b):
    if b==0:
      return "could not divide by zero"

    return func(a,b)
  return wrapper
@smart_division
def division(a,b):
  return a/b

print(division(20,10))
print(division(20,0))
'''

'''def division(a,b):
  if b == 0:
    return "could not divide by zero"
  return a/b
print(division(20,10))
print(division(20,0))
'''

import time
'''start_time=time.time()
total=0
for i in range(1,100000001):
  total+=i

print(total)
print(time.time()-start_time)

'''

def decorate_function(fn):
  def wrapper(*a,**k):
    start_time=time.time()
    fn(*a,**k)
    print(time.time()-start_time)
  return wrapper

@decorate_function
def example():
  print("Hello Everyone!")

@decorate_function
def example1(n):
  print(f"hello everyone {n}")

@decorate_function  
def example2(x,y):

  print(x+y)

example2(x=10,y=20)
example1(10)
example()

  
  

