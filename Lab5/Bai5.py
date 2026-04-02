import numpy as np
import matplotlib.pyplot as plt

# ----------------------
# Thiết lập seed để lặp lại kết quả
# ----------------------
np.random.seed(42)

# ======================
# 1. Random Walk 1 chiều, 100 bước
# ======================
num_steps = 100
steps = np.random.choice([-1, 1], size=num_steps)  # +1 hoặc -1 mỗi bước
walk = np.cumsum(steps)  # tính vị trí sau mỗi bước

# In kết quả
print("10 vị trí đầu tiên:", walk[:10])
print("Vị trí cuối cùng:", walk[-1])
print("Vị trí lớn nhất:", np.max(walk))
print("Vị trí nhỏ nhất:", np.min(walk))

# Vẽ đồ thị
plt.figure(figsize=(8,4))
plt.plot(walk, marker='o', markersize=3, linestyle='-')
plt.title("Random Walk 1 chiều (100 bước)")
plt.xlabel("Bước")
plt.ylabel("Vị trí")
plt.grid(True)
plt.tight_layout()
plt.show()

# ======================
# 2. 100 Random Walk, mỗi walk 100 bước
# ======================
num_walks = 100
steps_many = np.random.choice([-1, 1], size=(num_walks, num_steps))
walks_many = np.cumsum(steps_many, axis=1)  # cộng dồn theo hàng (mỗi walk)

final_positions = walks_many[:, -1]
num_positive = np.sum(final_positions > 0)
print("Số walk kết thúc dương:", num_positive)

hit_10 = np.any(np.abs(walks_many) >= 10, axis=1)
num_hit_10 = np.sum(hit_10)
print("Số walk chạm ngưỡng |10|:", num_hit_10)
