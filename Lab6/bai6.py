import pandas as pd

# Đọc file dữ liệu
df = pd.read_csv("diem_sinhvien.csv")

# Hiển thị thông tin tổng quan
print("Thông tin dữ liệu:")
df.info()

print("\n5 dòng đầu:")
print(df.head())

# Tính điểm trung bình
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

# Tạo cột xếp loại
df["XepLoai"] = df["DiemTB"].apply(xep_loai)

# Lọc sinh viên Khá trở lên
ket_qua = df[df["XepLoai"].isin(["Gioi", "Kha"])]

# Sắp xếp giảm dần theo điểm TB
ket_qua = ket_qua.sort_values(by="DiemTB", ascending=False)

# Lưu ra file CSV
ket_qua.to_csv("ketqua_xuly.csv", index=False, encoding="utf-8-sig")

# Hiển thị kết quả
print("\nDanh sách sinh viên Khá trở lên:")
print(ket_qua)

print("\nĐã lưu file ketqua_xuly.csv")