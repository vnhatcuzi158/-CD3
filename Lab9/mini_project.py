import pandas as pd

# =========================
# 1. ĐỌC DỮ LIỆU
# =========================
df = pd.read_csv("du_lieu_goc.csv")

print("=== DỮ LIỆU GỐC ===")
print(df)

# =========================
# 2. XỬ LÝ MISSING
# =========================
df["KhachHang"] = df["KhachHang"].fillna("ChuaCapNhat")
df["NgayDat"] = pd.to_datetime(df["NgayDat"], errors="coerce")

# =========================
# 3. XÓA TRÙNG
# =========================
df = df.drop_duplicates()

# =========================
# 4. CHUẨN HÓA DỮ LIỆU
# =========================

# Giá
df["Gia"] = df["Gia"].astype(str).str.replace(r"[^\d]", "", regex=True)
df["Gia"] = pd.to_numeric(df["Gia"], errors="coerce")

# Trạng thái
df["TrangThai"] = df["TrangThai"].str.strip().str.lower()

# =========================
# 5. XỬ LÝ NGOẠI LỆ
# =========================

# SoLuong < 0
df = df[df["SoLuong"] >= 0]

# Giá lỗi → thay bằng median
df["Gia"] = df["Gia"].fillna(df["Gia"].median())

# =========================
# 6. TẠO BIẾN MỚI
# =========================

# 1. Thành tiền
df["ThanhTien"] = df["SoLuong"] * df["Gia"]

# 2. Tháng
df["Thang"] = df["NgayDat"].dt.month

# 3. Nhóm giá
df["NhomGia"] = pd.cut(df["Gia"], bins=[0,100000,300000,1000000], labels=["Thap","TB","Cao"])

# =========================
# 7. XUẤT FILE
# =========================

df.to_csv("du_lieu_sach.csv", index=False)

print("\n=== DỮ LIỆU SẠCH ===")
print(df)   