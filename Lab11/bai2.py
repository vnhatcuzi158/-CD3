import pandas as pd
import matplotlib.pyplot as plt

# Tạo dữ liệu giả lập
data = {
    "Nhom": ["A", "A", "B", "B", "C", "C"],
    "GiaTri": [10, 15, 20, 25, 30, 35]
}

df = pd.DataFrame(data)

# Nhóm dữ liệu và tính trung bình
group_data = df.groupby("Nhom")["GiaTri"].mean()

print("Dữ liệu sau khi nhóm:")
print(group_data)

# Vẽ biểu đồ cột
group_data.plot(kind="bar", title="Giá trị trung bình theo nhóm")

plt.xlabel("Nhóm")
plt.ylabel("Giá trị trung bình")
plt.show()