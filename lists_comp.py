a = []

'''for i in range(5):
  a.append(i)
  
print(a)
'''

a = [i for i in range(5)]
print(a)

b = [{i:i**2} for i in range(1,10)]
print(b)
b = [(i,i**2) for i in range(1,10)]
print(b)
b = [[i,i**2] for i in range(1,10)]
print(b)

email = ["1@hotmail", "2@hotmail", "3@gmail", "4@hotmail", "5@gmail", "6@gmail"]
gmail_list = [i for i in email if i.endswith("@gmail")]
print(gmail_list)