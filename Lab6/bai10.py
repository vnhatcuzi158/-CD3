import pandas as pd

# Tạo dữ liệu giao dịch
data = {
    "MaHD": ["HD01","HD02","HD03","HD04","HD05","HD06","HD07","HD08","HD09","HD10","HD11","HD12"],
    "NhanVien": ["An","Binh","Chi","An","Dung","Chi","An","Binh","Dung","Chi","An","Binh"],
    "SoLuong": [1,5,2,3,1,4,2,6,1,2,1,3],
    "DonGia": [14500000,150000,2500000,750000,900000,450000,300000,180000,2500000,900000,14500000,300000]
}

# Tạo DataFrame
df = pd.DataFrame(data)

# Tính doanh thu từng giao dịch
df["DoanhThu"] = df["SoLuong"] * df["DonGia"]

# Hiển thị toàn bộ dữ liệu
print("Danh sách giao dịch:")
print(df)

# Tính tổng doanh thu theo nhân viên
tong_nv = df.groupby("NhanVien")["DoanhThu"].sum().reset_index()

# Sắp xếp giảm dần
tong_nv = tong_nv.sort_values(by="DoanhThu", ascending=False)

print("\nTổng doanh thu theo nhân viên:")
print(tong_nv)

# Nhân viên doanh thu cao nhất
print("\nNhân viên doanh thu cao nhất:")
print(tong_nv.iloc[0])