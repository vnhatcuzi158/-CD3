import pandas as pd

# Tạo dữ liệu khách hàng
data = {
    "MaKH": ["KH01","KH02","KH03","KH04","KH05","KH06","KH07","KH08"],
    "TenKH": ["Lan","Minh","Hung","Ha","Phuong","Toan","Ngoc","Tuan"],
    "SoDonHang": [12, 5, 8, 15, 4, 10, 6, 3],
    "TongChiTieu": [25000000, 7200000, 12500000, 31000000, 4300000, 9800000, 15000000, 2800000]
}

# Tạo DataFrame
df = pd.DataFrame(data)

# Hàm xếp loại khách hàng
def xep_loai(tien):
    if tien >= 20000000:
        return "VIP"
    elif tien >= 10000000:
        return "Than thiet"
    elif tien >= 5000000:
        return "Tiem nang"
    else:
        return "Thuong"

# Tạo cột xếp loại
df["XepLoaiKH"] = df["TongChiTieu"].apply(xep_loai)

# Hiển thị toàn bộ
print("Danh sách khách hàng:")
print(df)

# Lọc khách hàng VIP và thân thiết
print("\nKhách hàng VIP và thân thiết:")
print(df[df["XepLoaiKH"].isin(["VIP", "Than thiet"])])

# Sắp xếp theo chi tiêu giảm dần
print("\nDanh sách sắp xếp theo chi tiêu giảm dần:")
print(df.sort_values(by="TongChiTieu", ascending=False))

# Tính chi tiêu trung bình
print("\nChi tiêu trung bình:", df["TongChiTieu"].mean())