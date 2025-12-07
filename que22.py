s = input("Enter a string: ")

s = s.lower()

count = 0
vowels = "aeiou"

for ch in s:
    if ch in vowels:
        count += 1

print("Total vowels:", count)