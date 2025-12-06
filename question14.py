user_input = input("Enter elements of the list separated by commas: ")
my_list = [int(x) for x in user_input.split(',')]
target = int(input("Enter the number to search: "))

for num in my_list:
    if num == target:
        print(f"{target} found in the list")
        break
else:
    print(f"{target} not found in the list")