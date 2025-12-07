n = int(input("How many numbers: "))
lst = []

for i in range(n):
    lst.append(int(input("Enter number: ")))

lst_sorted = sorted(lst)

second_smallest = lst_sorted[1]
second_largest = lst_sorted[-2]

print("List:", lst)
print("Second Smallest:", second_smallest)
print("Second Largest:", second_largest)
