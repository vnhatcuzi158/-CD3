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

# Tạo Pivot Table theo lớp và xếp loại
pivot1 = pd.pivot_table(
    df,
    index="Lop",        # Hàng là Lop
    columns="XepLoai",  # Cột là XepLoai
    values="MaSV",      # Giá trị dùng để đếm
    aggfunc="count",    # Hàm tổng hợp: đếm số sinh viên
    fill_value=0        # Thay NaN bằng 0
)

# Hiển thị kết quả
print("Pivot Table: số lượng sinh viên theo lớp và xếp loại")
print(pivot1)