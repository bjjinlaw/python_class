# child class "IS A" Parent class
# Teacher "IS A" Person -> this is correct
# Dog "IS A" Person -> this is incorrect
'''
class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def walk(self):
        print(f"{self.name} is walking")

class Teacher(Person):
    def __init__(self, name, address, designation):
        #Person.__init__(self, name, address) # used in python2
        super().__init__(name, address)
        self.designation = designation
    
    def teach(self):
        print(f"{self.name} is teaching.")

class Student(Person):
    def __init__(self, name, address, roll_number):
        super().__init__(name, address)
        self.roll = roll_number

    def walk(self):
        super().walk()
        print(f"{self.name} is running")


t = Teacher("Ram", "Tokha", "science")
t.walk()
t.teach()
p = Person("sita", "ktm")
p.walk()

s = Student("bijay", "Chyasindol", "1234")
s.walk()
'''

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    


class Person(User):
    def __init__(self, username, password, name, address):
        super().__init__(username, password)
        self.name = name
        self.address = address

    def profile(self):
        print(f"name: {self.name}")
        print(f"address: {self.address}")
        print(f"username:{self.username}")





class Student(Person):
    def __init__(self,username, password, name, address, roll_number):
        super().__init__(username,password,name, address)
        self.roll = roll_number

    def walk(self):
        super().profile()
        print(f"his roll number is {self.roll}")


class Teacher(Person):
    def __init__(self, username, password, name, address, designation):
        #Person.__init__(self, name, address) # used in python2
        super().__init__(username, password,name, address)
        self.designation = designation
    
    def profile(self):
        super().profile()
        print(f"designation: {self.designation}")



t = Teacher("bjjinlaw", "12345", "ram", "tokha", "science")
t.profile()

s = Student("bjj", "1234", "shyam", "ktm", "nepali")
s.profile()
