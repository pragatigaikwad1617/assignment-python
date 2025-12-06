marks = []
while True:
    mark_input = input("Enter mark (or 'done' to finish): ")
    if mark_input.lower() == 'done':
        break
    try:
        mark = int(mark_input)
        marks.append(mark)
    except ValueError:
        print("Invalid input. Please enter a number or 'done'.")

if marks:
    failing_marks = [mark for mark in marks if mark < 40]
    min_mark = min(marks)
    max_mark = max(marks)
    average_mark = sum(marks) / len(marks)

    print(f"Failing marks: {failing_marks}")
    print(f"Minimum mark: {min_mark}")
    print(f"Maximum mark: {max_mark}")
    print(f"Average mark: {average_mark}")
else:
    print("No marks entered.")