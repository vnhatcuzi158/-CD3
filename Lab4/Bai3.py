import numpy as np

# 1. Dữ liệu doanh thu (7 ngày, 5 sản phẩm)
sales = np.array([
    [120, 150, 130, 140, 160],
    [125, 145, 128, 142, 158],
    [130, 155, 135, 150, 162],
    [135, 160, 140, 152, 168],
    [140, 165, 145, 155, 170],
    [138, 162, 142, 153, 169],
    [145, 170, 150, 160, 175]
])

print("=== MA TRẬN DOANH THU ===")
print(sales)

# 1. Tổng doanh thu theo ngày
daily_total = sales.sum(axis=1)
print("\n=== DOANH THU THEO NGÀY ===")
print(daily_total)

# 2. Tổng và trung bình theo sản phẩm
product_total = sales.sum(axis=0)
product_mean = sales.mean(axis=0)

print("\n=== TỔNG DOANH THU THEO SẢN PHẨM ===")
print(product_total)

print("\n=== DOANH THU TRUNG BÌNH THEO SẢN PHẨM ===")
print(product_mean)

# 3. Ngày cao nhất & sản phẩm tốt nhất
best_day = np.argmax(daily_total)
best_product = np.argmax(product_total)

print("\n=== CAO NHẤT ===")
print("Ngày doanh thu cao nhất:", best_day)
print("Sản phẩm bán tốt nhất:", best_product)

# 4. Tăng 8% sản phẩm 2 và 5
new_sales = sales.astype(float).copy()
new_sales[:, [1, 4]] *= 1.08

print("\n=== DOANH THU SAU ĐIỀU CHỈNH ===")
print(new_sales)

# 5. So sánh tổng trước và sau
before_total = sales.sum()
after_total = new_sales.sum()

print("\n=== SO SÁNH TỔNG DOANH THU ===")
print("Trước:", before_total)
print("Sau:", after_total)

# 6. Ngày doanh thu > trung bình
high_days = np.where(daily_total > daily_total.mean())[0]
print("\n=== NGÀY DOANH THU CAO HƠN TRUNG BÌNH ===")
print(high_days)

# 7. Sản phẩm ổn định nhất (std nhỏ nhất)
stable_product = np.argmin(sales.std(axis=0))
print("\n=== SẢN PHẨM ỔN ĐỊNH NHẤT ===")
print(stable_product)

# 8. Nhận xét
print("\n=== NHẬN XÉT ===")
print("- Một số sản phẩm có doanh thu cao và ổn định nên ưu tiên kinh doanh.")
print("- Sản phẩm có tổng doanh thu cao nhất là lựa chọn tốt để tập trung bán.")
print("- Sản phẩm ổn định giúp duy trì nguồn thu lâu dài.")
print("- Sau khi tăng giá/khuyến mãi, tổng doanh thu tăng rõ rệt.")
