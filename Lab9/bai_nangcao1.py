import pandas as pd

# 1. Đọc dữ liệu
df = pd.read_csv("tuyensinh.csv")

print("=== DỮ LIỆU BAN ĐẦU ===")
print(df)

# =========================
# 2. CHUẨN HÓA DỮ LIỆU
# =========================

# Họ tên
df["HoTen"] = df["HoTen"].fillna("ChuaCapNhat").str.strip().str.title()

# Giới tính
df["GioiTinh"] = df["GioiTinh"].str.strip().str.lower()

df["GioiTinh"] = df["GioiTinh"].replace({
    "nam": "Nam",
    "male": "Nam",
    "nu": "Nữ",
    "nữ": "Nữ",
    "female": "Nữ"
})

# Ngày sinh
df["NgaySinh"] = pd.to_datetime(df["NgaySinh"], errors="coerce")

# =========================
# 3. XỬ LÝ DỮ LIỆU THIẾU
# =========================

# Điền điểm bằng trung bình
for col in ["DiemToan", "DiemVan", "DiemAnh"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")
    df[col] = df[col].fillna(df[col].mean())

# =========================
# 4. PHÁT HIỆN ĐIỂM SAI
# =========================

for col in ["DiemToan", "DiemVan", "DiemAnh"]:
    df[col] = df[col].apply(lambda x: x if 0 <= x <= 10 else None)

# Điền lại bằng trung bình
for col in ["DiemToan", "DiemVan", "DiemAnh"]:
    df[col] = df[col].fillna(df[col].mean())

# =========================
# 5. TÍNH TỔNG ĐIỂM
# =========================

df["TongDiem"] = df["DiemToan"] + df["DiemVan"] + df["DiemAnh"]

# =========================
# 6. PHÂN NHÓM qcut
# =========================

df["XepHang"] = pd.qcut(df["TongDiem"], q=3, labels=["Thap", "TrungBinh", "Cao"])

# =========================
# 7. THỐNG KÊ THEO KHU VỰC
# =========================

tong_hop = df.groupby("KhuVuc").agg(
    SoLuong=("MaHS", "count"),
    DiemTB=("TongDiem", "mean")
)

# =========================
# 8. XUẤT FILE
# =========================

df.to_csv("tuyensinh_clean.csv", index=False)
tong_hop.to_csv("tuyensinh_thongke.csv")

print("\n=== SAU KHI XỬ LÝ ===")
print(df)

print("\n=== THỐNG KÊ ===")
print(tong_hop)