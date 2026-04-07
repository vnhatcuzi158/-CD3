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

# GroupBy nhiều điều kiện (Lop + GioiTinh) và tổng hợp
baocao = df.groupby(["Lop", "GioiTinh"])["DiemTB"].agg(
    SoLuong="count",
    TrungBinh="mean",
    CaoNhat="max",
    ThapNhat="min"
)

# Hiển thị kết quả
print("Báo cáo tổng hợp theo lớp và giới tính:")
print(baocao)