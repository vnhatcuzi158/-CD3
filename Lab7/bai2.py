import pandas as pd

# Đọc dữ liệu CSV đúng
df = pd.read_csv("diem_sinhvien_bai2.csv")

# Kiểm tra cột có đọc đúng chưa
print("Các cột hiện có trong DataFrame:", df.columns, "\n")

# Tính điểm trung bình học phần với trọng số 20%-30%-50%
df["DiemTB"] = 0.2 * df["DiemQT"] + 0.3 * df["DiemGK"] + 0.5 * df["DiemCK"]

# Hiển thị 5 dòng đầu
print("5 dòng đầu:")
print(df[["MaSV", "HoTen", "DiemTB"]].head(), "\n")

# Thống kê điểm trung bình
print("Thống kê điểm trung bình:")
print(df["DiemTB"].describe(), "\n")

# Sắp xếp sinh viên theo điểm trung bình từ cao xuống thấp
df_sorted = df.sort_values(by="DiemTB", ascending=False)
print("Sinh viên sắp xếp theo DiemTB từ cao xuống thấp:")
print(df_sorted[["MaSV", "HoTen", "DiemTB"]])