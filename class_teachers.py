class_teachers = {}
n = int(input("Enter number of classes: "))
for i in range(n):
    class_name = input("Class name: ")
    teacher_name = input("Teacher name: ")
    class_teachers[class_name] = teacher_name # Corrected line
print("Class-Teacher")
tea = input("Enter class to find teacher: ")
if tea in class_teachers:
    print(class_teachers[tea])
else:
    print("Class not found")


