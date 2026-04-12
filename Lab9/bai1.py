import pandas as pd

# Đọc dữ liệu
df = pd.read_csv("diem_sinhvien.csv")

print("=== DỮ LIỆU BAN ĐẦU ===")
print(df)

# 1. Kiểm tra giá trị thiếu
print("\n=== GIÁ TRỊ THIẾU ===")
print(df.isna().sum())

# 2. Điền giá trị thiếu (KHÔNG dùng inplace nữa)
df["DiemQT"] = df["DiemQT"].fillna(df["DiemQT"].mean())
df["DiemThi"] = df["DiemThi"].fillna(df["DiemThi"].mean())
df["HoTen"] = df["HoTen"].fillna("ChuaCapNhat")

# 3. Tính lại điểm tổng kết
df["DiemTK"] = 0.4 * df["DiemQT"] + 0.6 * df["DiemThi"]

# 4. Xếp loại
def xep_loai(diem):
    if diem >= 8:
        return "A"
    elif diem >= 6.5:
        return "B"
    elif diem >= 5:
        return "C"
    else:
        return "D"

df["XepLoai"] = df["DiemTK"].apply(xep_loai)

# 5. Xuất file
df.to_csv("diem_sinhvien_clean.csv", index=False)

print("\n=== SAU KHI LÀM SẠCH ===")
print(df)