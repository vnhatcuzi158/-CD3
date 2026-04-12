import pandas as pd

# 1. Đọc dữ liệu
df = pd.read_csv("donhang.csv")

print("=== DỮ LIỆU BAN ĐẦU ===")
print(df)

# 2. Kiểm tra trùng toàn bộ
print("\n=== DÒNG TRÙNG TOÀN BỘ ===")
print(df[df.duplicated()])

# 3. Kiểm tra trùng theo MaDon
print("\n=== TRÙNG THEO MaDon ===")
print(df[df.duplicated(subset=["MaDon"])])

# 4. Xóa trùng (giữ bản ghi đầu tiên)
df = df.drop_duplicates()
df = df.drop_duplicates(subset=["MaDon"], keep="first")

# 5. Tạo cột ThanhTien
df["ThanhTien"] = df["SoLuong"] * df["DonGia"]

# 6. Chuyển NgayDat về dạng ngày
df["NgayDat"] = pd.to_datetime(df["NgayDat"])

# 7. Sắp xếp theo NgayDat tăng dần
df = df.sort_values(by="NgayDat")

# 8. Xuất file mới
df.to_csv("donhang_clean.csv", index=False)

print("\n=== SAU KHI XỬ LÝ ===")
print(df)