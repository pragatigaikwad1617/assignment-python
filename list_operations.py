numbers = [4, 1, 9, 3, 7, 1, 5]

numbers.sort()
numbers.append(10)
numbers.remove(1)
popped = numbers.pop()

print("Popped element:", popped)

if popped in numbers:
    print("Yes, popped element is still in the list.")
else:
    print("No, popped element is not in the list.")
