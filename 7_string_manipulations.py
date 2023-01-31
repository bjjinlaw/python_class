a = "My name is Bijay Magar."
'''print(len(a)) #prints length of string

print(a.find("B")) #finds in which index is character located.

print(a.count("M")) # counts how many times a letter is in string

print(a.index("n")) # prints index of character

print(a.count(" ")) # counts number of spaces

print(a[0])
print(a[1])
print(a[0:5])
print(a[-1])
print(a[-2])
print(a[0:])
print(a[1:])
print(a[:1])
print(a[:5])
print(a[-1:])
print(a[-4:])
print(a[:-4])
print(a[1:10:4])
print(a[1::2])
print(a[::2])
print(a[:10:])
print(a[-1:-6:-2])
print(a[-6:-1:2])
print(a[::-2])
print(a[:])
print(a.split(" "))
b=a.split()
print(b)
print(type(b))
print(a.startswith("M"))
print(a.endswith("."))
print(a*10)
print("a"*10)
print(a.replace("My", "his"))
print(a.upper())
print(a.title())
print(a.lower())
print(a.capitalize())
print(a.swapcase())
print("".join(reversed(a)))
print(a[::-1])
print(a.strip())
print(a.lstrip("M"))
print(a.rstrip("."))
print(a.strip("\n"))
print("hello" + " world" + "!")
print(':'.join(a))
print(a.isalnum())
print(a.isalpha())
print(a.isdigit())
print(a.istitle())
print(a.isupper())
print(a.islower())
print(a.endswith('.'))
f="a"
print(f.isalpha())'''
print(dir(a))
print(a.expandtabs())
print(a.format("a"))
print(a.format_map(1))
print(a.index("a"))
print(a.isascii())
print(a.ljust(4))
print(a.maketrans('a','a'))
print(a.removeprefix('a'))
print(a.removesuffix('a'))
print(a.removesuffix('My'))
print(a.rsplit())
print(a.translate('a'))
print(a.zfill(0))
print(a.isdecimal())
print(a.isnumeric())
print(a.isidentifier())
a = 10.345
b = 10.345
total = a+b
print("The sum of {0:.2f} and {1:.2f} is {2:.2f}".format(a,b,total))
