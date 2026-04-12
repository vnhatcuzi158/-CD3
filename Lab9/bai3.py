import pandas as pd

# 1. Đọc dữ liệu
df = pd.read_csv("nhansu.csv")

print("=== DỮ LIỆU BAN ĐẦU ===")
print(df)

# 2. Xóa khoảng trắng thừa trong HoTen
df["HoTen"] = df["HoTen"].str.strip()

# 3. Chuẩn hóa GioiTinh
df["GioiTinh"] = df["GioiTinh"].str.strip().str.lower()

df["GioiTinh"] = df["GioiTinh"].replace({
    "nam": "Nam",
    "male": "Nam",
    "nữ": "Nữ",
    "nu": "Nữ",
    "female": "Nữ"
})

# 4. Chuẩn hóa PhongBan (viết hoa chữ cái đầu)
df["PhongBan"] = df["PhongBan"].str.strip().str.title()

# 5. Đổi tên cột
df = df.rename(columns={
    "MaNV": "ma_nv",
    "HoTen": "ho_ten",
    "GioiTinh": "gioi_tinh",
    "PhongBan": "phong_ban",
    "Luong": "luong"
})

# 6. Xuất file mới
df.to_csv("nhansu_clean.csv", index=False)

print("\n=== SAU KHI CHUẨN HÓA ===")
print(df)