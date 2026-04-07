import pandas as pd

# Đọc dữ liệu CSV
df = pd.read_csv("diem_sinhvien_bai5.csv")

# Tính điểm trung bình nếu chưa có
df["DiemTB"] = 0.2 * df["DiemQT"] + 0.3 * df["DiemGK"] + 0.5 * df["DiemCK"]

# Hàm xếp loại
def xep_loai(diem):
    if diem >= 8.5:
        return "A"
    elif diem >= 7.0:
        return "B"
    elif diem >= 5.5:
        return "C"
    elif diem >= 4.0:
        return "D"
    else:
        return "F"

# Tạo cột XepLoai
df["XepLoai"] = df["DiemTB"].apply(xep_loai)

# Thống kê tần suất dữ liệu
print("Số lượng sinh viên theo giới tính:")
print(df["GioiTinh"].value_counts(), "\n")

print("Số lượng sinh viên theo lớp:")
print(df["Lop"].value_counts(), "\n")

print("Số lượng sinh viên theo chuyên ngành:")
print(df["ChuyenNganh"].value_counts(), "\n")

print("Số lượng sinh viên theo xếp loại:")
print(df["XepLoai"].value_counts())