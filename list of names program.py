#Program for Listing names
names = []

while True:
    name = input("Enter a name : ")
    if name.lower() == "quit":
        break
    names.append(name)

# Sort the names in alphabetical order
names.sort()

# Remove duplicates
unique_names = list(dict.fromkeys(names))

# Display the final sorted list
print("Final sorted list:")
for name in unique_names:
    print(name)

# Count and print the total number of names
total_names = len(unique_names)
print("Total number of names:", total_names)