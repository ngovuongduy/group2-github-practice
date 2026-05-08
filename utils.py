def search_student(students):
    keyword = input("Enter name or student ID to search: ").strip().lower()
    results = []
    for s in students:
        if keyword in s["name"].lower() or keyword in s["mssv"].lower():
            results.append(s)
    if len(results) == 0:
        print("No students found!")
        return
    print("\n===== SEARCH RESULTS =====")
    for s in results:
        print(f"Name: {s['name']}")
        print(f"ID: {s['mssv']}")
        print(f"GPA: {s['gpa']}")
        print("-" * 20)


def update_student(students):
    mssv = input("Enter student ID to update: ").strip()
    for s in students:
        if s["mssv"] == mssv:
            print(f"Current name: {s['name']}")
            print(f"Current GPA : {s['gpa']}")
            new_name = input("Enter new name (press Enter to skip): ").strip()
            if new_name:
                s["name"] = new_name
            while True:
                new_gpa = input("Enter new GPA (press Enter to skip): ").strip()
                if new_gpa == "":
                    break
                try:
                    gpa = float(new_gpa)
                    if 0 <= gpa <= 10:
                        s["gpa"] = gpa
                        break
                    print("GPA must be between 0 and 10!")
                except:
                    print("Invalid GPA!")
            print("Student updated successfully!")
            return
    print("Student not found!")


def statistics(students):
    if len(students) == 0:
        print("No students found!")
        return
    total = len(students)
    gpas  = [s["gpa"] for s in students]
    avg   = sum(gpas) / total
    best  = max(students, key=lambda s: s["gpa"])
    worst = min(students, key=lambda s: s["gpa"])

    excellent = 0
    good      = 0
    average   = 0
    weak      = 0
    for g in gpas:
        if g >= 8.5:
            excellent += 1
        elif g >= 7.0:
            good += 1
        elif g >= 5.0:
            average += 1
        else:
            weak += 1

    print("\n===== STATISTICS =====")
    print(f"Total students  : {total}")
    print(f"Average GPA     : {avg:.2f}")
    print(f"Highest GPA     : {best['gpa']} ({best['name']})")
    print(f"Lowest GPA      : {worst['gpa']} ({worst['name']})")
    print("-" * 20)
    print(f"Excellent (>=8.5): {excellent}")
    print(f"Good      (>=7.0): {good}")
    print(f"Average   (>=5.0): {average}")
    print(f"Weak      (< 5.0): {weak}")
