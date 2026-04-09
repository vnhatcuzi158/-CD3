import pandas as pd

# 🔥 1. Tạo dữ liệu mẫu (giả lập sales.csv)
data = {
    "MaDon": ["DH01","DH02","DH03","DH04","DH05","DH06"],
    "TenKH": ["A","B","C","D","E","F"],
    "DoanhThu": [500000, 1200000, 300000, 2000000, 800000, 1500000]
}

df = pd.DataFrame(data)

# Lưu file gốc
df.to_csv("sales.csv", index=False)
print("✅ Đã tạo sales.csv\n")

# 🔥 2. Đọc lại file CSV
df_read = pd.read_csv("sales.csv")

# 🔥 3. Đặt ngưỡng doanh thu
nguong = 1000000

# 🔥 4. Lọc đơn hàng doanh thu > ngưỡng
df_high = df_read[df_read["DoanhThu"] > nguong]

print("=== Đơn hàng doanh thu cao ===")
print(df_high)

# 🔥 5. Ghi ra CSV
df_high.to_csv("high_sales.csv", index=False)

# 🔥 6. Ghi ra Excel
df_high.to_excel("high_sales.xlsx", index=False)

print("\n✅ Đã ghi ra high_sales.csv và high_sales.xlsx")