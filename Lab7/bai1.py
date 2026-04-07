# bai1.py
import pandas as pd
import numpy as np

# Đọc dữ liệu từ file CSV
df = pd.read_csv("diem_sinhvien.csv")

# Hiển thị 5 dòng đầu tiên
print("5 dòng đầu tiên:")
print(df.head(), "\n")

# Hiển thị 5 dòng cuối cùng
print("5 dòng cuối cùng:")
print(df.tail(), "\n")

# Xem thông tin cấu trúc dữ liệu
print("Thông tin DataFrame:")
print(df.info(), "\n")

# Xem thống kê mô tả các cột số
print("Thống kê mô tả các cột số:")
print(df.describe())