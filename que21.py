phonebook = {"Aman": "9876543210", "Riya": "8765432109", "Karan": "7654321098"}

phonebook["Meera"] = "6543210987"
phonebook["Karan"] = "9998887776"
phonebook.pop("Riya")

name = input("Enter a name to search: ")

if name in phonebook:
    print("Number is:", phonebook.get(name))
else:
    print("Contact not found")