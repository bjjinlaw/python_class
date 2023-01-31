'''def max2(x,y):
  if x > y:
    return x
  return y
def max3(x,y,z):
  return max2(x,max2(y,z))
print(max3(input(),input(),input()))
'''

'''def max3(x,y,z):
  if x > y and x > z:
    return x

  if y > z and y > x:
    return y
  return z
  
print(max3(input(),input(),input()))    
'''


'''def sum1(a,b,c,d,e):
  return a+b+c+d+e

print(sum1(1,2,3,4,5))    
'''

'''def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print(sum([8, 2, 3, 0, 7]))
'''

'''def sum1(numbers):
  return sum(numbers)

print(sum1([1,2,3,4,5,6]))
'''

'''def multiply(numbers):
  total = 1
  for x in numbers:
    total *=x
  return total
print(multiply([1,2,3,4,5]))
'''

'''def reverse(string):
  return(string[::-1])

print(reverse("abcdefg"))
'''

'''def facto(numbers):
  if numbers == 0:
    return 1
  total = 1
  for i in range(0,numbers + 1):
    total*=i
    
  return total
print(facto(int(input())))
'''
'''def facto(n):
  if n == 0:
     return 1

  return n *facto(n-1)
n = int(input())
print(facto(n))
'''



  