'''
class Computer:

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram



    def config(self):
        print("Config is", self.cpu, self.ram)

com1 = Computer('i5','16gb')
com2 = Computer('i7','8gb')
#Computer.config(com1)
com1.config()
com2.config()
'''

class Computer:
    pass


c1 = Computer()
c2 = Computer()

print(id(c1))
print(id(c2))