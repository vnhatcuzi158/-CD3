import pandas as pd

# Tạo dữ liệu kho
data = {
    "MaSP": ["SP01","SP02","SP03","SP04","SP05","SP06"],
    "TenSP": ["Laptop","Chuot","Ban phim","USB","Loa","Webcam"],
    "TonDau": [5, 20, 15, 30, 10, 8],
    "NhapThem": [3, 10, 5, 20, 4, 2],
    "DaBan": [4, 18, 12, 35, 9, 3],
    "DonGia": [14500000,150000,300000,180000,750000,900000]
}

# Tạo DataFrame
df = pd.DataFrame(data)

# Tính tồn cuối
df["TonCuoi"] = df["TonDau"] + df["NhapThem"] - df["DaBan"]

# Tính giá trị tồn cuối
df["GiaTriTonCuoi"] = df["TonCuoi"] * df["DonGia"]

# Hiển thị toàn bộ
print("Danh sách tồn kho:")
print(df)

# Lọc sản phẩm sắp hết hàng
print("\nSản phẩm sắp hết hàng (TonCuoi <= 5):")
print(df[df["TonCuoi"] <= 5])

# Tìm sản phẩm có giá trị tồn cuối lớn nhất
print("\nSản phẩm có giá trị tồn cuối lớn nhất:")
print(df.loc[df["GiaTriTonCuoi"].idxmax()])