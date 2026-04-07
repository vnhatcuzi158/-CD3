import pandas as pd

# Đọc dữ liệu CSV (đã có DiemQT, DiemGK, DiemCK)
df = pd.read_csv("diem_sinhvien_bai2.csv")

# Tính điểm trung bình nếu chưa có
df["DiemTB"] = 0.2 * df["DiemQT"] + 0.3 * df["DiemGK"] + 0.5 * df["DiemCK"]

# Thống kê mô tả điểm trung bình
trung_binh = df["DiemTB"].mean()
diem_lon_nhat = df["DiemTB"].max()
diem_nho_nhat = df["DiemTB"].min()
do_lech_chuan = df["DiemTB"].std()

print("Thống kê mô tả điểm trung bình (DiemTB):")
print(f"Trung bình: {trung_binh:.2f}")
print(f"Lớn nhất: {diem_lon_nhat:.2f}")
print(f"Nhỏ nhất: {diem_nho_nhat:.2f}")
print(f"Độ lệch chuẩn: {do_lech_chuan:.2f}")