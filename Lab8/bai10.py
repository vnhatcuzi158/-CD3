import pandas as pd
import sqlite3

# 🔥 1. Kết nối SQLite (tạo file nếu chưa có)
conn = sqlite3.connect("shop.db")

# 🔥 2. Tạo bảng orders + dữ liệu mẫu
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    MaDon TEXT,
    TenKH TEXT,
    DoanhThu INTEGER
)
""")

# Xóa dữ liệu cũ (tránh bị trùng khi chạy lại)
cursor.execute("DELETE FROM orders")

# Thêm dữ liệu
data = [
    ("DH01","Nguyen Van A",500000),
    ("DH02","Tran Thi B",1200000),
    ("DH03","Le Van C",300000),
    ("DH04","Pham Thi D",2000000),
    ("DH05","Hoang Van E",800000)
]

cursor.executemany("INSERT INTO orders VALUES (?, ?, ?)", data)
conn.commit()

print("✅ Đã tạo database shop.db\n")

# 🔥 3. Đọc dữ liệu bằng pandas
df = pd.read_sql("SELECT * FROM orders", conn)

# 🔥 4. Hiển thị 5 dòng đầu
print("=== 5 dòng đầu ===")
print(df.head())

# 🔥 5. Tính tổng số đơn hàng
tong_don = len(df)

# 🔥 6. Tính tổng doanh thu
tong_dt = df["DoanhThu"].sum()

print("\n=== THỐNG KÊ ===")
print("Tổng số đơn hàng:", tong_don)
print("Tổng doanh thu:", tong_dt)

# 🔥 7. Đóng kết nối
conn.close()