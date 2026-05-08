# main.py - Chương trình chính

from student import add_student, display_students, delete_student, update_student
from utils   import search_student, statistics

def menu():
    # Dữ liệu mẫu để test
    students = [
        {"id": 1, "name": "Nguyen Van An",   "mssv": "SV001", "gpa": 3.8, "lop": "CNTT01"},
        {"id": 2, "name": "Tran Thi Bich",   "mssv": "SV002", "gpa": 3.2, "lop": "CNTT01"},
        {"id": 3, "name": "Le Hoang Nam",    "mssv": "SV003", "gpa": 2.7, "lop": "CNTT02"},
        {"id": 4, "name": "Pham Thi Lan",    "mssv": "SV004", "gpa": 3.5, "lop": "CNTT02"},
    ]

    while True:
        print("\n" + "=" * 42)
        print("      🎓 QUẢN LÝ SINH VIÊN")
        print("=" * 42)
        print("  1. Thêm sinh viên")
        print("  2. Hiển thị danh sách")
        print("  3. Tìm kiếm sinh viên")
        print("  4. Cập nhật thông tin")
        print("  5. Xóa sinh viên")
        print("  6. Thống kê")
        print("  0. Thoát")
        print("=" * 42)

        choice = input("  👉 Chọn chức năng: ").strip()

        if   choice == "1": add_student(students)
        elif choice == "2": display_students(students)
        elif choice == "3": search_student(students)
        elif choice == "4": update_student(students)
        elif choice == "5": delete_student(students)
        elif choice == "6": statistics(students)
        elif choice == "0":
            print("\n👋 Tạm biệt!")
            break
        else:
            print("❌ Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    menu()
