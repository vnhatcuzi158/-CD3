import pandas as pd
import numpy as np

# ======================
# 1. TẠO DỮ LIỆU
# ======================
data = {
    "MaSV": ["SV01", "SV02", "SV03", "SV03", "SV05", "SV06", "SV07", "SV08"],
    "Tuoi": [20, 21, 19, 19, None, 22, 35, 20],
    "GioiTinh": ["Nam", "Nữ", "nu", "nu", "Nam", "Nữ", "Nam", None],
    "GioTuHoc": [2.5, 3, None, 4, 2, 10, -1, 3.5],
    "GioMangXaHoi": [4, 5, 3.5, 3.5, 20, 2, 5, None],
    "DiemTB": [3.1, 2.8, 3.5, 3.5, 2.0, 3.8, 4.5, None]
}

df = pd.DataFrame(data)

print("===== DỮ LIỆU BAN ĐẦU =====")
print(df)

# ======================
# 2. KIỂM TRA
# ======================
print("\n===== THÔNG TIN DỮ LIỆU =====")
print("Kích thước:", df.shape)
print("Thiếu dữ liệu:\n", df.isnull().sum())

# ======================
# 3. LÀM SẠCH
# ======================
df = df.drop_duplicates(subset="MaSV")

# Chuẩn hóa giới tính
df["GioiTinh"] = df["GioiTinh"].replace({
    "nu": "Nữ",
    "Nữ": "Nữ",
    "Nam": "Nam"
})

df["GioiTinh"] = df["GioiTinh"].fillna("Không rõ")

# Điền thiếu
df["Tuoi"] = df["Tuoi"].fillna(df["Tuoi"].mean())
df["GioTuHoc"] = df["GioTuHoc"].fillna(df["GioTuHoc"].mean())
df["GioMangXaHoi"] = df["GioMangXaHoi"].fillna(df["GioMangXaHoi"].mean())
df["DiemTB"] = df["DiemTB"].fillna(df["DiemTB"].mean())

# ======================
# 4. XỬ LÝ NGOẠI LỆ
# ======================
df.loc[df["Tuoi"] > 30, "Tuoi"] = df["Tuoi"].mean()
df.loc[df["GioTuHoc"] < 0, "GioTuHoc"] = df["GioTuHoc"].mean()
df.loc[df["GioMangXaHoi"] > 12, "GioMangXaHoi"] = df["GioMangXaHoi"].mean()
df.loc[df["DiemTB"] > 4.0, "DiemTB"] = df["DiemTB"].mean()

print("\n===== DỮ LIỆU SAU LÀM SẠCH =====")
print(df)

# ======================
# 5. CHUẨN HÓA MIN-MAX
# ======================
cols = ["Tuoi", "GioTuHoc", "GioMangXaHoi", "DiemTB"]

df_minmax = df.copy()

for col in cols:
    min_val = df[col].min()
    max_val = df[col].max()
    
    if max_val - min_val == 0:
        df_minmax[col] = 0
    else:
        df_minmax[col] = (df[col] - min_val) / (max_val - min_val)

print("\n===== MIN-MAX =====")
print(df_minmax)

# ======================
# 6. CHUẨN HÓA Z-SCORE
# ======================
df_zscore = df.copy()

for col in cols:
    mean = df[col].mean()
    std = df[col].std()
    
    if std == 0:
        df_zscore[col] = 0
    else:
        df_zscore[col] = (df[col] - mean) / std

print("\n===== Z-SCORE =====")
print(df_zscore)

# ======================
# 7. NHẬN XÉT
# ======================
print("\n===== NHẬN XÉT =====")
print("- Dữ liệu ban đầu có lỗi: thiếu, trùng, sai định dạng, ngoại lệ")
print("- Sau xử lý: dữ liệu sạch và đồng nhất")
print("- Min-Max: đưa dữ liệu về [0,1]")
print("- Z-score: dữ liệu có trung bình ~0, độ lệch chuẩn ~1")
