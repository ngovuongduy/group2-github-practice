def add_student(students):

    name = input("Enter name: ")
    mssv = input("Enter student ID: ")

    while True:

        try:
            gpa = float(input("Enter GPA: "))

            if 0 <= gpa <= 10:
                break

            print("GPA must be between 0 and 10!")

        except:
            print("Invalid GPA!")

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

def delete_student(students):

    mssv = input("Enter student ID to delete: ")

    for s in students:

        if s["mssv"] == mssv:

            students.remove(s)

            print("Deleted successfully!")

            return

    print("Student not found!")