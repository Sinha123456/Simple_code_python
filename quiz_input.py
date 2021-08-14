names = input("enter list of names: ").title().split(",")
assignments = input("Enter the number of assignments: ").split(",")
grades = input("Enter a list of grades").split(",")

message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n."

for names, assignments, grades in zip(names, assignments, grades):


    print(message.format(names, assignments, grades, int(grades) + int(assignments)*2))
