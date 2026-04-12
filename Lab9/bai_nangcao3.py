import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# 1. Đọc dữ liệu
df = pd.read_csv("benhnhan.csv")

print("=== BAN ĐẦU ===")
print(df)

# =========================
# 2. CHUẨN HÓA PHÂN LOẠI
# =========================

# GioiTinh
df["GioiTinh"] = df["GioiTinh"].str.strip().str.lower()
df["GioiTinh"] = df["GioiTinh"].replace({
    "nam": "Nam",
    "male": "Nam",
    "nu": "Nữ",
    "female": "Nữ"
})

# ChanDoan
df["ChanDoan"] = df["ChanDoan"].fillna("KhongXacDinh")

# =========================
# 3. XỬ LÝ THIẾU
# =========================

num_cols = ["Tuoi", "HuyetApTamThu", "HuyetApTamTruong", "DuongHuyet"]

for col in num_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")
    df[col] = df[col].fillna(df[col].median())

# mode cho phân loại
df["GioiTinh"] = df["GioiTinh"].fillna(df["GioiTinh"].mode()[0])

# =========================
# 4. PHÁT HIỆN OUTLIER (IQR)
# =========================

for col in num_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    
    # thay outlier bằng median
    median = df[col].median()
    df[col] = df[col].apply(lambda x: median if x < lower or x > upper else x)

# =========================
# 5. ENCODING
# =========================

# Label Encoding thủ công
df["ChanDoan"] = df["ChanDoan"].map({
    "BinhThuong": 0,
    "TieuDuong": 1,
    "KhongXacDinh": 2
})

# =========================
# 6. SCALING
# =========================

scaler = MinMaxScaler()
df[num_cols] = scaler.fit_transform(df[num_cols])

# =========================
# 7. LƯU FILE
# =========================

df.to_csv("benhnhan_processed.csv", index=False)

print("\n=== SAU XỬ LÝ ===")
print(df)