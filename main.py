from student import add_student, display_students, delete_student
from utils   import search_student, update_student, statistics

def menu():
    students = []

    while True:
        print("\n===== STUDENT MANAGEMENT =====")
        print("1. Add student")
        print("2. Display all students")
        print("3. Search student")
        print("4. Update student")
        print("5. Delete student")
        print("6. Statistics")
        print("0. Exit")
        print("=" * 30)

        choice = input("Enter your choice: ").strip()

        if   choice == "1": add_student(students)
        elif choice == "2": display_students(students)
        elif choice == "3": search_student(students)
        elif choice == "4": update_student(students)
        elif choice == "5": delete_student(students)
        elif choice == "6": statistics(students)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    menu()
