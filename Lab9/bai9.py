import pandas as pd
import matplotlib.pyplot as plt

# 1. Đọc dữ liệu
df = pd.read_csv("moitruong.csv")

print("=== DỮ LIỆU BAN ĐẦU ===")
print(df)

# 2. Tính IQR
Q1 = df["NhietDo"].quantile(0.25)
Q3 = df["NhietDo"].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

# 3. Đánh dấu outlier
df["Outlier"] = (df["NhietDo"] < lower) | (df["NhietDo"] > upper)

# 4. Thống kê trước
print("\n=== TRƯỚC KHI XỬ LÝ ===")
print(df["NhietDo"].describe())
print("Số outlier:", df["Outlier"].sum())

# 5. Thay outlier bằng trung vị
median = df["NhietDo"].median()
df.loc[df["Outlier"], "NhietDo"] = median

# 6. Thống kê sau
print("\n=== SAU KHI XỬ LÝ ===")
print(df["NhietDo"].describe())

# 7. Vẽ boxplot
plt.figure()
df["NhietDo"].plot.box()
plt.title("Boxplot NhietDo sau khi xử lý")
plt.show()

# 8. Xuất file
df.to_csv("moitruong_clean.csv", index=False)

print("\n=== DỮ LIỆU SAU CÙNG ===")
print(df)