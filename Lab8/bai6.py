import pandas as pd

# 🔥 1. Tạo dữ liệu
data = {
    "MaSP": ["SP01","SP02","SP03","SP04","SP05","SP06","SP07","SP08","SP09","SP10"],
    "TenSP": ["Ao thun","Quan jean","Giay","Mu","Ao khoac","Tui xach","Dep","Non","Ao so mi","Quan short"],
    "SoLuong": [15,25,10,30,18,50,12,8,40,5],
    "DonGia": [150000,350000,500000,120000,450000,600000,90000,70000,200000,180000]
}

df = pd.DataFrame(data)

# 🔥 2. Lưu file Excel
df.to_excel("inventory.xlsx", sheet_name="HangHoa", index=False)
print("✅ Đã tạo file inventory.xlsx\n")

# 🔥 3. Đọc lại file Excel
df_read = pd.read_excel("inventory.xlsx", sheet_name="HangHoa")

# 🔥 4. Hiển thị 10 dòng đầu
print("=== 10 dòng đầu ===")
print(df_read.head(10))

# 🔥 5. Lọc hàng tồn kho < 20
df_thieu = df_read[df_read["SoLuong"] < 20]

print("\n=== Hàng tồn kho < 20 ===")
print(df_thieu)

# 🔥 6. DataFrame mới
print("\n=== DataFrame sau khi lọc ===")
print(df_thieu)