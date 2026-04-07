import pandas as pd
import numpy as np

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

# Tạo cột KetQua: Đỗ nếu >=4.0, Trượt nếu <4.0
df["KetQua"] = np.where(df["DiemTB"] >= 4.0, "Do", "Truot")

# Thống kê số lượng đỗ/trượt theo lớp
so_luong = pd.crosstab(df["Lop"], df["KetQua"])
print("Số lượng đỗ/trượt theo lớp:")
print(so_luong)

# Thống kê tỷ lệ đỗ/trượt theo lớp (%)
ty_le = pd.crosstab(df["Lop"], df["KetQua"], normalize="index") * 100
print("\nTỷ lệ đỗ/trượt theo lớp (%):")
print(ty_le.round(2))