import pandas as pd
import matplotlib.pyplot as plt

# Tạo dữ liệu giả lập
data = {
    "X": [1, 2, 3, 4, 5, 6, 7],
    "Y": [2, 4, 5, 4, 5, 7, 8]
}

df = pd.DataFrame(data)

# Vẽ scatter plot
df.plot(kind="scatter", x="X", y="Y", title="Mối quan hệ giữa X và Y")

plt.xlabel("X")
plt.ylabel("Y")
plt.show()