import pandas as pd

# 1. Đọc dữ liệu
df = pd.read_csv("chitieu.csv")

print("=== DỮ LIỆU BAN ĐẦU ===")
print(df)

# 2. Kiểm tra giao dịch không hợp lệ
loi = df[df["SoTien"] <= 0]
print("\n=== GIAO DỊCH KHÔNG HỢP LỆ ===")
print(loi)

# 3. Loại bỏ dữ liệu không hợp lệ
df = df[df["SoTien"] > 0]

# 4. Chia mức chi tiêu
bins = [0, 100000, 300000, float("inf")]
labels = ["Thap", "TrungBinh", "Cao"]

df["MucChiTieu"] = pd.cut(df["SoTien"], bins=bins, labels=labels)

# 5. Thống kê số giao dịch theo mức
thong_ke = df["MucChiTieu"].value_counts()

# 6. Tổng chi tiêu theo nhóm
tong_chi = df.groupby("NhomChiTieu")["SoTien"].agg("sum")

# 7. Xuất file
df.to_csv("chitieu_clean.csv", index=False)

print("\n=== SAU KHI XỬ LÝ ===")
print(df)

print("\n=== THỐNG KÊ MỨC CHI TIÊU ===")
print(thong_ke)

print("\n=== TỔNG CHI THEO NHÓM ===")
print(tong_chi)