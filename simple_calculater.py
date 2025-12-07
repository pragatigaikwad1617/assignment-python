print("1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Exit")

ch = int(input("Enter choice (1-5): "))

if 1 <= ch <= 4:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

match ch:
    case 1: print("Result =", a + b)
    case 2: print("Result =", a - b)
    case 3: print("Result =", a * b)
    case 4: print("Result =", a / b)
    case 5: print("Exiting...")
    case _: print("Invalid choice")
