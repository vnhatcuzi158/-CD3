import pandas as pd

# Đọc file KHÔNG có header
df = pd.read_csv(
    "scores_no_header.csv",
    header=None,
    names=["MaSV", "HoTen", "Lop", "DiemQT", "DiemThi"]
)

# Hiển thị dữ liệu
print("=== Dữ liệu ===")
print(df)

# Hiển thị thông tin
print("\n=== Thông tin dữ liệu ===")
df.info()