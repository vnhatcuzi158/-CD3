import pandas as pd

# Tạo dữ liệu
data = {
    "MaSV": ["SV01","SV02","SV03","SV04","SV05","SV06","SV07","SV08","SV09","SV10"],
    "GioTuHoc": [3, 2, 1, 4, 2.5, 1.5, 3.5, 2, 1, 4],
    "SoBuoiNghi": [1, 2, 4, 0, 1, 3, 0, 2, 5, 1],
    "DiemCC": [9, 8, 6, 10, 8, 6, 9, 8, 5, 10],
    "DiemCuoiKy": [8, 7.5, 6, 9, 8, 6.5, 8.5, 7, 5.5, 9]
}

# Tạo DataFrame
df = pd.DataFrame(data)

# Tính điểm trung bình
df["DiemTB"] = 0.3 * df["DiemCC"] + 0.7 * df["DiemCuoiKy"]

# Hàm phân nhóm học tập
def nhom_hoc_tap(row):
    if row["GioTuHoc"] >= 3 and row["SoBuoiNghi"] <= 1:
        return "Tich cuc"
    elif row["GioTuHoc"] >= 2 and row["SoBuoiNghi"] <= 2:
        return "Binh thuong"
    else:
        return "Can ho tro"

# Tạo cột nhóm học tập
df["NhomHocTap"] = df.apply(nhom_hoc_tap, axis=1)

# Hiển thị toàn bộ dữ liệu
print("Danh sách sinh viên:")
print(df)

# Lọc sinh viên theo điều kiện
print("\nSinh viên tự học > 2h và nghỉ <= 2 buổi:")
print(df[(df["GioTuHoc"] > 2) & (df["SoBuoiNghi"] <= 2)])