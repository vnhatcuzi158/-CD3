import pandas as pd

# Tạo dữ liệu hóa đơn
data = {
    "MaHD": ["HD01","HD02","HD03","HD04","HD05","HD06","HD07","HD08","HD09","HD10"],
    "NgayBan": ["2026-04-01","2026-04-01","2026-04-02","2026-04-02","2026-04-03",
                "2026-04-03","2026-04-04","2026-04-04","2026-04-05","2026-04-05"],
    "TenSP": ["Laptop","Chuot","Man hinh","USB","Loa","Tai nghe","Laptop","Webcam","Ban phim","Man hinh"],
    "SoLuong": [1, 5, 2, 10, 3, 4, 1, 2, 6, 1],
    "DonGia": [14500000,150000,2500000,180000,750000,450000,14500000,900000,300000,2500000],
    "NhanVien": ["An","Binh","An","Chi","Dung","Ha","An","Chi","Binh","Ha"]
}

# Tạo DataFrame
df = pd.DataFrame(data)

# Tính thành tiền
df["ThanhTien"] = df["SoLuong"] * df["DonGia"]

# Hiển thị toàn bộ
print("Danh sách hóa đơn:")
print(df)

# Top 5 hóa đơn giá trị cao nhất
print("\nTop 5 hóa đơn có giá trị cao nhất:")
print(df.sort_values(by="ThanhTien", ascending=False).head(5))

# Lọc hóa đơn >= 3 triệu
print("\nHóa đơn có ThanhTien >= 3,000,000:")
print(df[df["ThanhTien"] >= 3000000])

# Tổng doanh thu
tong_doanh_thu = df["ThanhTien"].sum()
print("\nTổng doanh thu:", tong_doanh_thu)