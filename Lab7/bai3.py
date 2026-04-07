import pandas as pd

# Đọc dữ liệu CSV đã có DiemQT, DiemGK, DiemCK
df = pd.read_csv("diem_sinhvien_bai2.csv")

# Tính điểm trung bình (nếu chưa có)
df["DiemTB"] = 0.2 * df["DiemQT"] + 0.3 * df["DiemGK"] + 0.5 * df["DiemCK"]

# Hàm xếp loại sinh viên
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

# Hiển thị 5 dòng đầu với xếp loại
print("5 sinh viên đầu tiên với điểm trung bình và xếp loại:")
print(df[["HoTen", "DiemTB", "XepLoai"]].head(), "\n")

# Thống kê số lượng sinh viên theo xếp loại
print("Số lượng sinh viên theo xếp loại:")
print(df["XepLoai"].value_counts())