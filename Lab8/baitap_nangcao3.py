import pandas as pd
import requests

# 🔥 1. Gọi API công khai (fake store API)
url = "https://fakestoreapi.com/products"

try:
    response = requests.get(url)
    data = response.json()
    print("✅ Lấy dữ liệu từ API thành công\n")
except:
    print("❌ Không gọi được API → dùng dữ liệu giả lập\n")
    # fallback nếu mất mạng
    data = [
        {"id": 1, "title": "Ao thun", "category": "Thoi trang", "price": 150000},
        {"id": 2, "title": "Quan jean", "category": "Thoi trang", "price": 350000},
        {"id": 3, "title": "Giay", "category": "Giay dep", "price": 500000}
    ]

# 🔥 2. Chuyển sang DataFrame
df = pd.DataFrame(data)

# 🔥 3. Chọn các trường quan trọng
df_selected = df[["id", "title", "category", "price"]]

print("=== Dữ liệu đã chọn ===")
print(df_selected.head())

# 🔥 4. Lưu ra CSV
df_selected.to_csv("products_api.csv", index=False)

print("\n✅ Đã lưu file products_api.csv")