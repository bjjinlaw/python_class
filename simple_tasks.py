#colors = ["yellow", "red", "orange", "blue", "violet", "red", "white"]
#colors_to_remove = ["red", "violet"]
colors = []
colors_to_remove = []
for k in range(7):
  l1 = input("enter colors: ")
  colors.append(l1)
print(colors)
  
for m in range(4):
  l2 = input("enter colors to remove: ")
  colors_to_remove.append(l2)

for j in colors:
  for i in colors_to_remove:
    if i in colors:
      colors.remove(i)
print(colors)