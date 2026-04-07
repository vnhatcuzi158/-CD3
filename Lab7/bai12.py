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

# Phân nhóm điểm học lực
bins = [0, 5, 7, 8.5, 10]                        # Giới hạn các nhóm
labels = ["<5", "5-6.9", "7-8.4", ">=8.5"]      # Nhãn nhóm
df["NhomDiem"] = pd.cut(df["DiemTB"], bins=bins, labels=labels, right=False)

# Thống kê số lượng sinh viên theo từng nhóm điểm của mỗi lớp
bang_nhom = pd.crosstab(df["Lop"], df["NhomDiem"])

# Hiển thị kết quả
print("Số lượng sinh viên theo nhóm điểm và lớp:")
print(bang_nhom)