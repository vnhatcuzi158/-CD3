import pandas as pd

# Tạo dữ liệu dạng dict
data = {
    "MaSV": ["SV01", "SV02", "SV03", "SV04", "SV05"],
    "HoTen": ["An", "Bình", "Chi", "Dũng", "Hà"],
    "Lop": ["CNTT1", "CNTT1", "CNTT2", "CNTT2", "CNTT1"],
    "DiemQT": [7.0, 8.5, 6.0, 9.0, 8.0],
    "DiemThi": [7.5, 8.0, 6.5, 9.5, 8.5]
}

# Tạo DataFrame
df = pd.DataFrame(data)

# Hiển thị toàn bộ DataFrame
print("Danh sách sinh viên:")
print(df)

# Chọn cột HoTen và DiemThi
print("\nChọn cột HoTen và DiemThi:")
print(df[["HoTen", "DiemThi"]])

# Tạo cột Điểm Trung Bình
df["DiemTB"] = 0.4 * df["DiemQT"] + 0.6 * df["DiemThi"]

# Hiển thị DataFrame sau khi thêm cột
print("\nDataFrame sau khi thêm cột DiemTB:")
print(df)