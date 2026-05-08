def search_student(students):
    keyword = input("Nhập tên hoặc MSSV cần tìm: ").lower()
    results = [s for s in students if keyword in s["name"].lower() or keyword in s["mssv"].lower()]
    if results:
        for s in results:
            print(f"🔍 Tìm thấy: {s['name']} - {s['mssv']} - GPA: {s['gpa']}")
    else:
        print("Không tìm thấy!")
