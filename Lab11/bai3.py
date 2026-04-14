import pandas as pd
import matplotlib.pyplot as plt

# Tạo dữ liệu giả lập
data = {
    "GiaTri": [10, 12, 15, 20, 22, 25, 30, 32, 35, 40, 45, 50]
}

df = pd.DataFrame(data)

# Vẽ histogram
df["GiaTri"].plot(kind="hist", bins=5, title="Phân phối dữ liệu")

plt.xlabel("Giá trị")
plt.ylabel("Tần suất")
plt.show()