import pandas as pd

# 1. Đọc dữ liệu
df = pd.read_csv("suckhoe.csv")

print("=== DỮ LIỆU BAN ĐẦU ===")
print(df)

# 2. Phát hiện tuổi không hợp lệ
tuoi_loi = df[(df["Tuoi"] <= 0) | (df["Tuoi"] > 100)]
print("\n=== TUỔI KHÔNG HỢP LỆ ===")
print(tuoi_loi)

# 3. Phát hiện thiếu cân nặng, chiều cao
thieu_dl = df[df["CanNang"].isna() | df["ChieuCao"].isna()]
print("\n=== THIẾU CÂN NẶNG / CHIỀU CAO ===")
print(thieu_dl)

# 4. Điền giá trị thiếu bằng trung vị
df["CanNang"] = pd.to_numeric(df["CanNang"], errors="coerce")
df["ChieuCao"] = pd.to_numeric(df["ChieuCao"], errors="coerce")

df["CanNang"] = df["CanNang"].fillna(df["CanNang"].median())
df["ChieuCao"] = df["ChieuCao"].fillna(df["ChieuCao"].median())

# 5. Chuẩn hóa nhóm máu
df["NhomMau"] = df["NhomMau"].str.strip().str.upper()

df["NhomMau"] = df["NhomMau"].replace({
    "A": "A",
    "B": "B",
    "AB": "AB",
    "O": "O"
})

# 6. Tính BMI
df["BMI"] = df["CanNang"] / ((df["ChieuCao"] / 100) ** 2)

# 7. Xuất file
df.to_csv("suckhoe_clean.csv", index=False)

print("\n=== SAU KHI XỬ LÝ ===")
print(df)