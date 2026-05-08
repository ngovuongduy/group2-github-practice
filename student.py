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