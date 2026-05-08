def add_student(students):

    name = input("Enter name: ")
    mssv = input("Enter student ID: ")

    gpa = float(input("Enter GPA: "))

    student = {
        "name": name,
        "mssv": mssv,
        "gpa": gpa
    }

    students.append(student)

    print("Student added successfully!")

def display_students(students):

    if len(students) == 0:
        print("No students found!")
        return

    print("\n===== STUDENT LIST =====")

    for s in students:

        print(f"Name: {s['name']}")
        print(f"ID: {s['mssv']}")
        print(f"GPA: {s['gpa']}")
        print("-" * 20)