import pandas as pd

# Tạo dữ liệu trực tiếp
data = {
    "name": ["An", "Binh", "Chi", "Dung", "Em"],
    "age": [20, 21, 19, 22, 20],
    "score": [8.5, 7.0, 9.0, 6.5, 8.0]
}

df = pd.DataFrame(data)

print("5 dòng đầu:")
print(df.head())

print("\nThông tin dữ liệu:")
print(df.info())

print("\nThống kê mô tả:")
print(df.describe())