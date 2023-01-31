
#for <variable> in <iterable_object>:
  # code for execution
'''
a = [10,20,30,40,50,60]
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])
for i in range(1,101):
  print(i)

# range(start, stop, step)
# range(10) => start=0, stop=9, step=1
# range(1,10) => start=1, stop=9, step=1
# range(1,10,2) =. start=1, stop=9, step=2


for i in range(2,101,2):
  print(i)

  
for i in range(100,0,-2):
  print(i)'''
total=0
for i in range(1,11):
  total+=i
  
print(total)

print(sum(list(range(1,11))))
print(sum(x for x in range(1,11)))
print(sum(range(1,11)))

print(sum(range(2, 21, 2)))

total = 0
for i in range(2,21,2):
  total +=i
  
print(total)

# take 10 input of student name
# append them in a list and print
# make sure, first letter of every name is capitalized

list1=[]
for i in range(1,6):
  slist = input("student name: ")
  list1.append(slist.title())

for i in list1:
  print(i)
