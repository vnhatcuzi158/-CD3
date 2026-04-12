import pandas as pd

# 1. Đọc dữ liệu
df = pd.read_csv("sanpham.csv")

print("=== DỮ LIỆU BAN ĐẦU ===")
print(df)

# 2. Làm sạch cột Gia (xóa ký tự tiền tệ, dấu phẩy)
df["Gia"] = df["Gia"].str.replace(r"[^\d]", "", regex=True)

# 3. Chuyển Gia sang số
df["Gia"] = df["Gia"].astype(float)

# 4. Chuẩn hóa DanhMuc (chữ thường)
df["DanhMuc"] = df["DanhMuc"].str.strip().str.lower()

# 5. Loại bỏ sản phẩm tồn kho âm
df = df[df["SoLuongTon"] >= 0]

# 6. Sắp xếp theo giá giảm dần
df = df.sort_values(by="Gia", ascending=False)

# 7. Xuất file
df.to_csv("sanpham_clean.csv", index=False)

print("\n=== SAU KHI XỬ LÝ ===")
print(df)