'''x = ()				# empty tuple
x = (0,)			# one item tuple
x = (0, 1, 2, "abc")            # four item tuple: indexed x[0]..x[3]
x = 0, 1, 2, "abc"              # parenthesis are optional
x = (0, 1, 2, 3, (1, 2))        # nested subtuples
y = x[0]		      	# indexed item
y = x[4][0]                    	# indexed subtuple
x = (0, 1) * 2                  # repeat
x = (0, 1, 2) + (3, 4)         	# concatenation
for item in x: print item    	# iterate through tuple
b = 3 in x			# test tuple membership
'''
'''x = (0,1,2,3,(1,2))
y=x[3]
print(y)
x = (0,1)*2
print(x)
x = (0,1,2)+(0,1,4)
print(x)'''
b = (1,2,3)
'''c = (2,3,4)
print(b+c)
print(b*2)
for item in b:
  print(item)
d = 3 not in b
print(d)
print(dir(tuple))
c = c.count(3)
print(c)
'''
c = b.index(2)
print(c)
b = list(b)
print(b)
b = tuple(b)
print(b)
b = set(b)
print(b)
import sys
x = (1,2,3)
z=sys.getsizeof(x)
y=[1,2,3]
s=sys.getsizeof(y)
print(z)
print(s)