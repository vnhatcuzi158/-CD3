import pandas as pd

# Đọc file CSV
df = pd.read_csv("diem_sinhvien.csv")

# 5 dòng đầu
print("5 dòng đầu:")
print(df.head())

# 5 dòng cuối
print("\n5 dòng cuối:")
print(df.tail())

# Thông tin dữ liệu
print("\nThông tin dữ liệu:")
df.info()

# Thống kê mô tả
print("\nThống kê mô tả:")
print(df.describe())

# Kích thước dữ liệu
print("\nKích thước dữ liệu:", df.shape)

# Tên các cột
print("Tên các cột:", df.columns.tolist())