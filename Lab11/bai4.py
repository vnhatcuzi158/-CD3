import pandas as pd
import matplotlib.pyplot as plt

# Tạo dữ liệu (có thêm giá trị ngoại lệ)
data = {
    "GiaTri": [10, 12, 15, 20, 22, 25, 30, 32, 35, 40, 100]
}

df = pd.DataFrame(data)

# Vẽ boxplot
df.boxplot(column="GiaTri")

plt.title("Boxplot phát hiện ngoại lệ")
plt.ylabel("Giá trị")
plt.show()  