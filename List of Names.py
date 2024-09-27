#Program to enter a list of names
names = []
while True: 
    values = input("Enter names: ")
    if values =="stop":
      break
names.append(values)

print(names)
