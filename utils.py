def search_student(students):
    print("\n--- TÌM KIẾM SINH VIÊN ---")
    keyword = input("Nhập tên hoặc MSSV: ").strip().lower()

    if not keyword:
        print("❌ Vui lòng nhập từ khóa!")
        return

    results = [
        s for s in students
        if keyword in s["name"].lower() or keyword in s["mssv"].lower()
    ]

    if results:
        print(f"\n🔍 Tìm thấy {len(results)} kết quả:")
        print(f"{'ID':<5} {'Họ và tên':<25} {'MSSV':<12} {'GPA':<6} {'Lớp'}")
        print("-" * 60)
        for s in results:
            print(f"{s['id']:<5} {s['name']:<25} {s['mssv']:<12} {s['gpa']:<6} {s['lop']}")
    else:
        print(f"😔 Không tìm thấy với từ khóa '{keyword}'")


def statistics(students):
    print("\n--- THỐNG KÊ ---")
    if not students:
        print("📭 Chưa có dữ liệu.")
        return

    total = len(students)
    gpas  = [s["gpa"] for s in students]
    avg   = sum(gpas) / total

    xuat_sac = sum(1 for g in gpas if g >= 3.6)
    gioi     = sum(1 for g in gpas if 3.2 <= g < 3.6)
    kha      = sum(1 for g in gpas if 2.5 <= g < 3.2)
    trung    = sum(1 for g in gpas if g < 2.5)

    best = max(students, key=lambda s: s["gpa"])
    worst = min(students, key=lambda s: s["gpa"])

    print(f"📊 Tổng sinh viên  : {total}")
    print(f"📈 GPA trung bình  : {avg:.2f}")
    print(f"🏆 GPA cao nhất    : {best['gpa']} ({best['name']})")
    print(f"📉 GPA thấp nhất   : {worst['gpa']} ({worst['name']})")
    print(f"\n🎓 Phân loại học lực:")
    print(f"   - Xuất sắc (≥3.6) : {xuat_sac} sinh viên")
    print(f"   - Giỏi   (3.2-3.6): {gioi} sinh viên")
    print(f"   - Khá    (2.5-3.2): {kha} sinh viên")
    print(f"   - Trung bình (<2.5): {trung} sinh viên")
