n = int(input("Enter how many numbers: "))
lst = []

for i in range(n):
    num = int(input("Enter number: "))
    lst.append(num)

positive = []
negative = []

for x in lst:
    if x >= 0:
        positive.append(x)
    else:
        negative.append(x)

print("Original List:", lst)
print("Positive List:", positive)
print("Negative List:", negative)