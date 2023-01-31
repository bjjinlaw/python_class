# map, filter
#lambda
'''
def product(x,y):
    return x*y

def get_product(fn):
    return fn(10,20)

print(get_product(product))
print(get_product(lambda x,y:x*y))

a = lambda x,y:x*y
print(a(10,20))
'''

# map(func, iterable_object)

a = [3,9,8,17,15,90]
'''
b = []
for i in a:
    b.append(i+1)

print(b)
'''
'''
def increase_by_one(n):
    return n + 1

output = list(map(increase_by_one, a))
print(output)
output = list(map(lambda n:n+1,a))
print(output)
'''

'''
name_list=["ram","shyam","hari","sita"]
def cap(n):
    return n.title()

a = list(map(cap,name_list))
print(a)

a = list(map(lambda name:name.title(),name_list))
print(a)

a=list(map(str.capitalize,name_list))
print(a)
'''

# filter(func, iterable_object)
# this function should always return boolean value

'''
a = [1,2,3,4,5,6,7,8,9,10]

output = list(filter(lambda n:n % 2 == 0,a))
print(output)

'''
'''
a = "2,4,6,d,8,9,e,4"

output = sum(map(int, filter(str.isdigit,a.split(","))))
print(output)
'''

marks_of_students = [
    {
        "name":"ram",
        "marks":{"maths":40,"eng":50,"nep":60}
    },
    {
        "name":"hari",
        "marks":{"maths":40,"eng":70,"nep":60}
    },
    {
        "name":"sita",
        "marks":{"maths":40,"eng":45,"nep":60}
    },
]

marks=[]
name=[]

for i in marks_of_students:
    marks.append(sum(i.get('marks').values()))
    name.append(i.get('name'))
#print(marks)
#print(name)

new_list=list(zip(marks,name))
#print(new_list)

if new_list[0][0]>(new_list[1][0] and new_list[2][0]):
    first = new_list[0][0]
    


if new_list[1][0]>(new_list[0][0] and new_list[2][0]):
    first = new_list[1][0]


else:
    first= new_list[2][0]

if new_list[0][0]<(new_list[1][0] and new_list[2][0]):
    third = new_list[0][0]


if new_list[1][0]<(new_list[0][0] and new_list[2][0]):
    third = new_list[1][0]


else:
    third= new_list[2][0]


print(f"first is ")










