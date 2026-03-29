# Dữ liệu mẫu
scores = [7.5, 8.0, 4.5, 9.0, 6.0, 5.5, 8.5, 3.0]

# 1. Danh sách điểm đạt (>=5)
passed = [s for s in scores if s >= 5]

# 2. Danh sách bình phương của điểm đạt
squared = [s**2 for s in passed]

# 3. Tạo dict xếp loại
grading = {
    i+1: (
        "A" if s >= 8 else
        "B" if s >= 6.5 else
        "C" if s >= 5 else
        "F"
    )
    for i, s in enumerate(scores)
}

# In kết quả
print("Danh sách điểm ban đầu:")
print(scores)

print("\nĐiểm đạt (>=5):")
print(passed)

print("\nBình phương điểm đạt:")
print(squared)

print("\nXếp loại sinh viên:")
for k, v in grading.items():
    print(f"Sinh viên {k}: {v}")
