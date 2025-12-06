user_input = input("Enter elements of the list separated by commas: ")
my_list = user_input.split(',')
reversed_list = my_list[::-1]
print("Original list:", my_list)
print("Reversed list:", reversed_list)