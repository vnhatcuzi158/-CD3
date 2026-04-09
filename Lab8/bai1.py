import pandas as pd

# Đọc file CSV
df = pd.read_csv("students.csv")

# Hiển thị 5 dòng đầu
print("=== 5 dòng đầu ===")
print(df.head())

# In số dòng và số cột
print("\n=== Kích thước dữ liệu ===")
print("Số dòng, số cột:", df.shape)

# In tên các cột
print("\n=== Danh sách cột ===")
print(df.columns.tolist())