import pandas as pd

# 1. Đọc dữ liệu
df = pd.read_csv("lienhe.csv")

print("=== DỮ LIỆU BAN ĐẦU ===")
print(df)

# 2. Chuẩn hóa email (chữ thường)
df["Email"] = df["Email"].str.lower()

# 3. Kiểm tra email hợp lệ (regex)
pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
df["EmailHopLe"] = df["Email"].str.contains(pattern, regex=True)

# 4. Tách đầu số điện thoại (3 số đầu)
df["DauSo"] = df["SoDienThoai"].astype(str).str.extract(r'^(\d{3})')

# 5. Xóa khoảng trắng địa chỉ
df["DiaChi"] = df["DiaChi"].str.strip()

# 6. Trích xuất domain email
df["Domain"] = df["Email"].str.extract(r'@(.+)$')

# 7. Xuất file
df.to_csv("lienhe_clean.csv", index=False)

print("\n=== SAU KHI XỬ LÝ ===")
print(df)
