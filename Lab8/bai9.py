import pandas as pd
import json

# 🔥 1. Tạo file JSON (nếu chưa có)
data = [
    {"MaSP": "SP01", "TenSP": "Ao thun", "Nhom": "Thoi trang", "Gia": 150000},
    {"MaSP": "SP02", "TenSP": "Quan jean", "Nhom": "Thoi trang", "Gia": 350000},
    {"MaSP": "SP03", "TenSP": "Giay sneaker", "Nhom": "Giay dep", "Gia": 500000},
    {"MaSP": "SP04", "TenSP": "Mu luoi trai", "Nhom": "Phu kien", "Gia": 120000}
]

with open("products.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("✅ Đã tạo products.json\n")

# 🔥 2. Đọc JSON → DataFrame
df = pd.read_json("products.json")

# 🔥 3. Hiển thị các trường cơ bản
print("=== Dữ liệu sản phẩm ===")
print(df[["MaSP", "TenSP", "Nhom", "Gia"]])

# 🔥 4. Nhận xét
print("\n=== NHẬN XÉT ===")
print("- JSON có cấu trúc dạng key-value (linh hoạt)")
print("- CSV dạng bảng, phân tách bằng dấu ,")
print("- JSON dùng nhiều trong web/API")
print("- CSV đơn giản, dễ xử lý trong Excel")