import pandas as pd

# =========================
# 1. ĐỌC FILE
# =========================
df1 = pd.read_csv("banhang_thang1.csv")
df2 = pd.read_csv("banhang_thang2.csv")
df3 = pd.read_csv("banhang_thang3.csv")

# =========================
# 2. CHUẨN HÓA TÊN CỘT
# =========================
def chuan_hoa_cot(df):
    df.columns = df.columns.str.lower().str.strip()
    return df

df1 = chuan_hoa_cot(df1)
df2 = chuan_hoa_cot(df2)
df3 = chuan_hoa_cot(df3)

# đổi về cùng tên
df1 = df1.rename(columns={
    "madon": "ma_don",
    "ngaydat": "ngay_dat",
    "sanpham": "san_pham",
    "soluong": "so_luong",
    "gia": "gia"
})

df3 = df3.rename(columns={
    "madon": "ma_don",
    "ngaydat": "ngay_dat",
    "sanpham": "san_pham",
    "soluong": "so_luong",
    "gia": "gia"
})

# df2 đã đúng

# =========================
# 3. GHÉP DỮ LIỆU
# =========================
df = pd.concat([df1, df2, df3], ignore_index=True)

# =========================
# 4. XỬ LÝ GIÁ TIỀN
# =========================
df["gia"] = df["gia"].astype(str).str.replace(r"[^\d]", "", regex=True)
df["gia"] = df["gia"].astype(float)

# =========================
# 5. CHUẨN HÓA NGÀY
# =========================
df["ngay_dat"] = pd.to_datetime(df["ngay_dat"], errors="coerce")

# =========================
# 6. XỬ LÝ TRÙNG MÃ ĐƠN
# =========================
df = df.drop_duplicates(subset=["ma_don"], keep="first")

# =========================
# 7. TÍNH DOANH THU
# =========================
df["thanh_tien"] = df["so_luong"] * df["gia"]

# =========================
# 8. BÁO CÁO
# =========================

# Doanh thu theo tháng
df["thang"] = df["ngay_dat"].dt.to_period("M")
doanh_thu = df.groupby("thang")["thanh_tien"].sum()

# Top 5 sản phẩm
top_sp = df.groupby("san_pham")["thanh_tien"].sum().sort_values(ascending=False).head(5)

# Đơn lỗi (ngày bị lỗi)
don_loi = df[df["ngay_dat"].isna()]

# =========================
# 9. XUẤT FILE
# =========================
df.to_csv("banhang_clean.csv", index=False)
doanh_thu.to_csv("doanhthu_thang.csv")
top_sp.to_csv("top_sanpham.csv")

print("\n=== DỮ LIỆU SAU XỬ LÝ ===")
print(df)

print("\n=== DOANH THU THEO THÁNG ===")
print(doanh_thu)

print("\n=== TOP 5 SẢN PHẨM ===")
print(top_sp)

print("\n=== ĐƠN LỖI ===")
print(don_loi)