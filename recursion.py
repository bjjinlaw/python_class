'''
def factorial(num):
    if num==0:
        return 1

    return num*factorial(num-1)

print(factorial(int(input("Enter any number"))))
'''

def multiplication(num, x=0):
    if x==11:
        return
    print(f"{num} x {x}={num*x}")
    x+=1
    return multiplication(num,x)

multiplication(10)


def exponent(base, power):
    if power==0:
        return 1        

    return base*exponent(base,power-1)


print(exponent(int(input("enter base: ")), int(input("enter power: "))))
