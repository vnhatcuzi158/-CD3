import pandas as pd

# 🔥 1. Tạo 3 file CSV (mỗi file tên cột khác nhau)

# Tháng 1
jan = pd.DataFrame({
    "MaDon": ["DH01","DH02"],
    "TenKH": ["A","B"],
    "DoanhThu": [500000, 1200000]
})
jan.to_csv("sales_jan.csv", index=False)

# Tháng 2 (tên cột khác)
feb = pd.DataFrame({
    "OrderID": ["DH03","DH04"],
    "Customer": ["C","D"],
    "Revenue": [300000, 2000000]
})
feb.to_csv("sales_feb.csv", index=False)

# Tháng 3 (lại khác nữa)
mar = pd.DataFrame({
    "MaDonHang": ["DH05","DH06"],
    "TenKhach": ["E","F"],
    "Tien": [800000, 1500000]
})
mar.to_csv("sales_mar.csv", index=False)

print("✅ Đã tạo 3 file CSV\n")

# 🔥 2. Đọc các file
df_jan = pd.read_csv("sales_jan.csv")
df_feb = pd.read_csv("sales_feb.csv")
df_mar = pd.read_csv("sales_mar.csv")

# 🔥 3. Chuẩn hóa tên cột về cùng schema
df_jan.columns = ["MaDon", "TenKH", "DoanhThu"]
df_feb.columns = ["MaDon", "TenKH", "DoanhThu"]
df_mar.columns = ["MaDon", "TenKH", "DoanhThu"]

# 🔥 4. Ghép dữ liệu (concat)
df_all = pd.concat([df_jan, df_feb, df_mar], ignore_index=True)

print("=== Dữ liệu sau khi ghép ===")
print(df_all)

# 🔥 5. Lưu thành file mới
df_all.to_csv("sales_q1.csv", index=False)

print("\n✅ Đã lưu file sales_q1.csv")