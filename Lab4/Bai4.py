import numpy as np

# 1. Dữ liệu
stock = np.array([35, 8, 12, 5, 40, 18, 7, 22, 9, 15])
min_stock = np.array([20, 15, 15, 10, 25, 20, 12, 18, 12, 15])
price = np.array([30, 25, 28, 22, 35, 20, 18, 24, 19, 21])

print("=== TỒN KHO HIỆN TẠI ===")
print(stock)

# 1. Mặt hàng thiếu
need_import = np.maximum(min_stock - stock, 0)
print("\n=== SỐ LƯỢNG CẦN NHẬP ===")
print(need_import)

# 2. Trạng thái
status = np.where(stock < min_stock, "Thiếu hàng", "Đủ hàng")
print("\n=== TRẠNG THÁI ===")
print(status)

# 3. Chi phí nhập thêm (chỉ tính hàng thiếu)
cost = need_import * price
print("\n=== CHI PHÍ NHẬP TỪNG MẶT HÀNG ===")
print(cost)

# 4. Tổng chi phí
total_cost = cost.sum()
print("\n=== TỔNG CHI PHÍ NHẬP ===")
print(total_cost)

# 5. Top 3 thiếu nhiều nhất
top3_shortage = np.argsort(need_import)[::-1][:3]
print("\n=== TOP 3 THIẾU NHIỀU NHẤT ===")
print(top3_shortage)
print("Số lượng thiếu:", need_import[top3_shortage])

# 6. Giới hạn nhập tối đa 20
limited_need = np.clip(need_import, 0, 20)
print("\n=== SỐ LƯỢNG SAU KHI GIỚI HẠN ===")
print(limited_need)

# 7. Tổng chi phí sau giới hạn
limited_total_cost = (limited_need * price).sum()
print("\n=== TỔNG CHI PHÍ SAU GIỚI HẠN ===")
print(limited_total_cost)

# 8. Nhận xét
print("\n=== NHẬN XÉT ===")
print("- Kho có nhiều mặt hàng đang thiếu so với mức tối thiểu.")
print("- Một số mặt hàng thiếu số lượng lớn cần ưu tiên nhập trước.")
print("- Việc giới hạn nhập giúp kiểm soát chi phí hiệu quả hơn.")
print("- Cần theo dõi tồn kho thường xuyên để tránh thiếu hụt nghiêm trọng.")
