import pandas as pd

df = pd.read_csv("khaosat.csv")

# 1. Chuẩn hóa CoLamThem (DÙNG MAP)
df["CoLamThem"] = df["CoLamThem"].str.strip().str.lower()

df["CoLamThem"] = df["CoLamThem"].map({
    "yes": 1,
    "y": 1,
    "có": 1,
    "no": 0,
    "n": 0,
    "không": 0
})

# 2. Chuẩn hóa MucDoHaiLong
df["MucDoHaiLong"] = df["MucDoHaiLong"].astype(str).str.lower()

df["MucDoHaiLong"] = df["MucDoHaiLong"].replace({
    "rat hai long": 5,
    "hai long": 4,
    "binh thuong": 3,
    "khong hai long": 2,
    "rat khong hai long": 1
})

df["MucDoHaiLong"] = pd.to_numeric(df["MucDoHaiLong"], errors="coerce")

# 3. Đổi tên cột
df = df.rename(columns={
    "MaSV": "ma_sv",
    "GioHocMoiNgay": "gio_hoc_moi_ngay",
    "MucDoHaiLong": "muc_do_hai_long",
    "CoLamThem": "co_lam_them"
})

# 4. Loại giờ học âm
df = df[df["gio_hoc_moi_ngay"] >= 0]

# 5. Thống kê
print("\n=== THỐNG KÊ ===")
print(df["co_lam_them"].value_counts())

print("\n=== SAU KHI XỬ LÝ ===")
print(df)