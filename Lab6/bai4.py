import pandas as pd

# Đọc file CSV
df = pd.read_csv("diem_sinhvien.csv")

# Tạo cột Điểm Trung Bình
df["DiemTB"] = 0.4 * df["DiemQT"] + 0.6 * df["DiemThi"]

# Hàm xếp loại
def xep_loai(diem):
    if diem >= 8.5:
        return "Gioi"
    elif diem >= 7.0:
        return "Kha"
    elif diem >= 5.5:
        return "Trung binh"
    else:
        return "Yeu"

# Tạo cột Xếp loại
df["XepLoai"] = df["DiemTB"].apply(xep_loai)

# Lọc sinh viên có điểm TB >= 8
print("Sinh viên có DiemTB >= 8:")
print(df[df["DiemTB"] >= 8])

# Đổi tên cột
df = df.rename(columns={"HoTen": "TenSinhVien"})

# Đặt MaSV làm index
df = df.set_index("MaSV")

# Hiển thị kết quả cuối
print("\nDataFrame sau khi xử lý:")
print(df)