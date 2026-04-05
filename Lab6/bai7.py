import pandas as pd

# Tạo dữ liệu sản phẩm
data = {
    "MaSP": ["SP01", "SP02", "SP03", "SP04", "SP05", "SP06", "SP07", "SP08"],
    "TenSP": ["Chuot", "Ban phim", "Man hinh", "USB", "Laptop", "Loa", "Tai nghe", "Webcam"],
    "LoaiHang": ["Phu kien", "Phu kien", "Thiet bi", "Phu kien", "Thiet bi", "Thiet bi", "Phu kien", "Thiet bi"],
    "DonGia": [150000, 300000, 2500000, 180000, 14500000, 750000, 450000, 900000],
    "SoLuongTon": [25, 18, 7, 40, 5, 12, 20, 8]
}

# Tạo DataFrame
df = pd.DataFrame(data)

# Tính giá trị tồn kho
df["GiaTriTonKho"] = df["DonGia"] * df["SoLuongTon"]

# Hiển thị toàn bộ danh sách
print("Danh sách sản phẩm:")
print(df)

# Lọc sản phẩm có đơn giá > 500000
print("\nSản phẩm có đơn giá > 500000:")
print(df[df["DonGia"] > 500000])

# Sắp xếp theo giá trị tồn kho giảm dần
print("\nSắp xếp theo giá trị tồn kho giảm dần:")
print(df.sort_values(by="GiaTriTonKho", ascending=False))

# Lọc sản phẩm có số lượng tồn < 10
print("\nSản phẩm có số lượng tồn < 10:")
print(df[df["SoLuongTon"] < 10])