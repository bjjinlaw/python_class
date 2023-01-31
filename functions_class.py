'''def welcome():
  print("welcome students")
  
welcome() # call for function execution
# welcome # call by reference
'''
'''def welcome(name, address): # parameters
  print("welcome",name)
  print("welcome",address)
#name = input("enter your name: ")
#address = input("enter address: ")
welcome(input("enter you name: "), input("enter your address: ")) # arguements
'''
'''def welcome(name, address, contact): # parameters
  print(f"welcome {name}")
  print(f"welcome {address}")
  print(f"{contact}")
#name = input("enter your name: ")
#address = input("enter address: ")
#welcome(input("enter you name: "), input("enter your address: ", input("enter your contact no: "))) # arguements

welcome("bijay", "tokha", "9823390335") # positional arguements
welcome(contact="9823390335", name="bijay", address="tokha")
'''

'''def addition(num1,num2=1):
  print(num1+num2)

addition(10)
addition(10,5)
'''


'''def addition1(num1, num2):
  print(num1+num2)

def addition2(num1, num2):
  return num1 + num2

print(addition2(1,2))
a=addition1(10,20)
print(f"addition: {a}")
res= addition2(10,20)
print(f"addition2: {res}")

'''


'''def multiple_positional_arguments(*a):
 print(a)
  
multiple_arguments(1,2,3,4,5, "python", "ramesh")
'''

def multiple_keyword_arguments(**a):
  print(a)
  
multiple_keyword_arguments(name="ram", contact="9823", address="tokha")

  
  
  
