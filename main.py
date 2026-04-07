class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("------")


students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter details for student", i + 1)

    name = input("Enter name: ")
    marks = int(input("Enter marks: "))

    s = Student(name, marks)
    students.append(s)

print("\nStudent Details:")
for s in students:
    s.display()