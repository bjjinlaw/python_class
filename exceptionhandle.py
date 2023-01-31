'''try:
    # block of code
except Exception:
    # block of code
except ValueError:
    # block of code
except TypeError:
    # block of code
else:
    # block of code

finally:
    # block of code
'''
try:
    a = int(input("enter first number: "))
    b = int(input("enter second number: "))
    
except ValueError:
    print("cannot convert to integer")
else:
    sum = f"Sum of {a} and {b} is {a+b}"
    print(sum)


name = input("Enter your name: ")
print(f"Name: {name}")
