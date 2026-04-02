import numpy as np

# ======================
# 1. Dữ liệu số lượng và giá
# ======================
quantity = np.array([
    [10, 12, 9, 14],
    [5, 7, 8, 6],
    [20, 18, 25, 22]
])
price = np.array([15000, 25000, 10000])  # giá từng sản phẩm

# ======================
# 2. Doanh thu từng sản phẩm theo ngày
# ======================
# reshape để broadcast đúng
revenue = quantity * price.reshape(3,1)
print("Doanh thu từng sản phẩm theo ngày:\n", revenue)

# ======================
# 3. Tổng doanh thu từng sản phẩm
# ======================
sum_product = np.sum(revenue, axis=1)
print("Tổng doanh thu từng sản phẩm:", sum_product)

# ======================
# 4. Tổng doanh thu từng ngày
# ======================
sum_day = np.sum(revenue, axis=0)
print("Tổng doanh thu từng ngày:", sum_day)

# ======================
# 5. Ngày doanh thu cao nhất
# ======================
max_day_index = np.argmax(sum_day)  # index bắt đầu từ 0
print("Ngày doanh thu cao nhất: Ngày", max_day_index + 1)

# ======================
# 6. Tỷ trọng doanh thu từng sản phẩm
# ======================
ratio = sum_product / np.sum(sum_product)
print("Tỷ trọng doanh thu (%):", np.round(ratio*100, 2))
