# Tạo danh sách sinh viên (mỗi sinh viên là 1 tuple)
students = [
    ("SV01", "Nguyễn Văn A", 7.5),
    ("SV02", "Trần Thị B", 8.2),
    ("SV03", "Lê Văn C", 6.8),
    ("SV04", "Phạm Thị D", 9.0),
    ("SV05", "Hoàng Văn E", 5.5),
    ("SV06", "Đỗ Thị F", 8.7),
    ("SV07", "Nguyễn Văn G", 7.9),
    ("SV08", "Bùi Thị H", 9.5)
]

# 1. In toàn bộ danh sách sinh viên
print("Danh sách sinh viên:")
for sv in students:
    print(f"Mã: {sv[0]}, Tên: {sv[1]}, Điểm: {sv[2]}")

# 2. Tìm sinh viên có điểm cao nhất
max_sv = students[0]
for sv in students:
    if sv[2] > max_sv[2]:
        max_sv = sv

print("\nSinh viên có điểm cao nhất:")
print(f"Mã: {max_sv[0]}, Tên: {max_sv[1]}, Điểm: {max_sv[2]}")

# 3. Tính điểm trung bình của cả lớp
tong_diem = 0
for sv in students:
    tong_diem += sv[2]

diem_tb = tong_diem / len(students)
print(f"\nĐiểm trung bình của lớp: {diem_tb:.2f}")

# 4. In danh sách sinh viên có điểm >= 8
print("\nSinh viên có điểm >= 8:")
for sv in students:
    if sv[2] >= 8:
        print(f"Mã: {sv[0]}, Tên: {sv[1]}, Điểm: {sv[2]}")
