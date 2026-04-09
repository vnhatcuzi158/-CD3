import pandas as pd

# 🔥 Ép kiểu MaKH về chuỗi
df = pd.read_csv("customers.csv", dtype={"MaKH": str})

# Hiển thị dữ liệu
print("=== Dữ liệu ===")
print(df)

# Kiểm tra kiểu dữ liệu từng cột
print("\n=== Kiểu dữ liệu ===")
print(df.dtypes)