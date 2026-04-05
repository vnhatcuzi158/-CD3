import pandas as pd

# Tạo Series lưu điểm sinh viên
diem = pd.Series(
    [7.5, 8.0, 6.5, 9.0, 8.5],
    index=["SV01", "SV02", "SV03", "SV04", "SV05"]
)

# Hiển thị toàn bộ Series
print("Danh sách điểm:")
print(diem)

# Hiển thị 2 phần tử đầu
print("\nHai phần tử đầu:")
print(diem.head(2))

# Điểm lớn nhất
print("\nĐiểm lớn nhất:", diem.max())

# Điểm trung bình
print("Điểm trung bình:", diem.mean())

# Lọc sinh viên có điểm >= 8
print("\nSinh viên có điểm >= 8:")
print(diem[diem >= 8])