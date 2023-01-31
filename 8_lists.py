'''a = [1, 2, 'bijay', 3.5]
print("the length of a is:", len(a))
a.append(3)
print(a)
a.append("hello")
print(a)
a.insert(0,'hi')
print(a)
a.remove("bijay")
print(a)
a.remove(2)
print(a)
gadgets1 = ['mobile', 'laptop', 'tab']
gadgets2 = ['pc', 'mouse', 'smartwatch']
gadgets1.extend(gadgets2)
print(gadgets1)
gadgets1.extend(['keyboard'])
print(gadgets1)
a.pop(0)
print(a)
a.pop(0)
print(a)
nums = [x for x in range(1,11)]
print(nums)
nums.pop()
print(nums)
print("was pc in gadgets1:", "pc" in gadgets1)
print("was trackpad not in gadgets1:", "trackpad" not in gadgets1)
#print(gadgets1[::-1])
gadgets1.reverse()
print(gadgets1)
for items in gadgets1[::-1]:
  print(items)
#print(nums)
nums=[2,4,3,1,5,6,2,4]
print(nums)
nums.sort()
print(nums)
alpha=['b','a','D','c']
alpha.sort()
print(alpha)
nums1=[2,4,3,1,5,6]
print(sorted(nums1))
print(nums1)
'''
'''e = [1,2,3,4,5]
temp = e[2]
e[2]=e[0]
e[0]=temp
print(e)

e[0],e[2]=e[2],e[0]
print(e)
'''

'''nums = [1,2,3,4,5,6,7,8,9,10]
prime_nums = [2,3,5,7,11,13]
for num in nums:
  if num in prime_nums:
    print(num, end= " ")
'''

'''a = [1,2,3,5.6,4.5,8,12]
sum = sum(a)
average = sum/len(a)   
print(average) 
'''
a = [1,2,3,5.6,4.5,8,12]
total = 0
i = 0
while i < len(a):
  total = total + a[i]
  i = i + 1
  
avg = total/len(a)
print("the average of the list is: {:.2f}".format(avg))

