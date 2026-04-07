import pandas as pd

# Đọc dữ liệu CSV
df = pd.read_csv("diem_sinhvien_bai5.csv")

# Tính điểm trung bình nếu chưa có
df["DiemTB"] = 0.2 * df["DiemQT"] + 0.3 * df["DiemGK"] + 0.5 * df["DiemCK"]

# Hàm xếp loại
def xep_loai(diem):
    if diem >= 8.5:
        return "A"
    elif diem >= 7.0:
        return "B"
    elif diem >= 5.5:
        return "C"
    elif diem >= 4.0:
        return "D"
    else:
        return "F"

# Tạo cột XepLoai
df["XepLoai"] = df["DiemTB"].apply(xep_loai)

# Tổng hợp theo chuyên ngành
tong_hop_cn = df.groupby("ChuyenNganh").agg(
    SoSinhVien=("MaSV", "count"),
    DiemTrungBinh=("DiemTB", "mean")
)

# Số sinh viên đạt loại A hoặc B
tyle_ab = df[df["XepLoai"].isin(["A", "B"])].groupby("ChuyenNganh")["MaSV"].count()

# Thêm cột số đạt AB, điền 0 nếu NaN
tong_hop_cn["SoDatAB"] = tyle_ab
tong_hop_cn["SoDatAB"] = tong_hop_cn["SoDatAB"].fillna(0)

# Tỷ lệ % sinh viên đạt AB
tong_hop_cn["TyLeDatAB"] = tong_hop_cn["SoDatAB"] / tong_hop_cn["SoSinhVien"] * 100

# Hiển thị kết quả
print("Báo cáo tổng hợp theo chuyên ngành:")
print(tong_hop_cn.round(2))