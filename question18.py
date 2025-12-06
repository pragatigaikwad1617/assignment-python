# Create tuple
n = int(input("How many numbers? "))
lst = []

for i in range(n):
    lst.append(int(input("Enter number: ")))

t = tuple(lst)
print("Tuple:", t)

# Add or remove
choice = input("Add or Remove? ")

if choice == "add":
    x = int(input("Enter number to add: "))
    t = t + (x,)
    print("Updated tuple:", t)

elif choice == "remove":
    x = int(input("Enter number to remove: "))
    if x in t:
        lst = list(t)
        lst.remove(x)
        t = tuple(lst)
        print("Updated tuple:", t)
    else:
        print("Number not in tuple")