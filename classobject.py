# Object Oriented Programming
# Class and Object
# Encapsulation
# Inheritance
# Polymorphism
# Abstraction

class Projector:
    def __init__(self,color,model,year):
        self.color = color
        self.year = year
        self.model = model
    
    def visualise(self):
        print(f"Projector of model {self.model} is visualising")

    def description(self):
        print(f"Colors: {self.color}")
        print(f"Model: {self.model}")
        print(f"year: {self.year}")

    def __str__(self):
        return self.model

    def __repr__(self):
        return self.model
    
#p = Projector(input("enter color: "), int(input("enter year")), input("enter model"))
#print(p.color)
#print(p.year)
#print(p.model)
'''
projectors = []
for i in range(3):
    color = input("enter color: ")
    model = input("enter model: ")
    year = input("enter year: ")
    
    p = Projector(color,model,year)
    projectors.append(p)


print(projectors)
'''
'''
p1=Projector("White", "NEC", 2022)
p2=Projector("Black", "ACER", 2021)
p3=Projector("blue", "Ntorque", 2023)

p1.visualise()
p2.visualise()
p1.description()
p2.description()
p3.visualise()
p3.description()

print(p1)
print(p1.__dict__)
'''
'''
class Student:
    def __init__(self, _id, name, contact, address):
        self._id = _id
        self.name = name
        self.contact = contact
        self.address = address
        self.total_attendance = 0

    def update_attendance(self):
        self.total_attendance +=1

    def view_attendance(self):
        return self.total_attendance
    
s = Student(1, "Ram", "2343", "Ktm")
s2 = Student(2,"Shyam", "34534", "Tokha")
s2.update_attendance()
s.update_attendance()
s2.update_attendance()
s.update_attendance()
print(s.view_attendance())
print(s2.view_attendance())
# print(Student.view_attendance(s))

class Product:
    def __init__(self, name, price):
        self.name = name
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price > 0:
            self.__price = price


tshirt = Product("Tshirt", 500)
jacket = Product("Jacket", 1000)
print(tshirt._Product__price)
print(tshirt.price)
print(f"Before setting: {tshirt.price}")
tshirt.price=200
print(f"After setting: {tshirt.price}")
'''
'''
class Calculator:
    def __init__(self, num1, num2):
        self.a = num1
        self.b = num2

    def add(self):
        return self.a + self.b
    
    def difference(self):
        return self.a - self.b
    
    def product(self):
        return self.a * self.b
    
    def division(self):
        return self.a / self.b

    @staticmethod
    def square_root(num):
        return num**0.5

c = Calculator(10,25)
print(c.add())
print(Calculator.square_root(25))
'''
'''
class Student:
    college = "ABC College" # class or static variable

    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

print(Student.college)
s = Student("Ram", "23423")
print(s.college)
print(s.__dict__)
'''
'''
class User:
    def __init__(self, username, password):
        self.username= username
        self.password = password

    @classmethod

    def create_user_with_random_pasword(cls, username):
        return cls(username, "Default_password")

u = User("ram@gmail.com", "Demo12345")
print(u.__dict__)

u2 = User.create_user_with_random_pasword("hari@gmail.com")
print(u2.__dict__)
'''

class ProductPriceError(Exception):
    pass


class Product:
    def __init__(self, name, price):
        self.name = name
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter    
    def price(self, price):
        if price <= 0:
            raise ProductPriceError("Price cannot be les than zero")
        self.__price = price

tshirt = Product("Tshirt", "-100")

try:
    tshirt.price = -100
    print(f"Without exception: {tshirt.price}")
except ProductPriceError as msg:
    print(msg)
    #print(f"After exception: {tshirt.price}")