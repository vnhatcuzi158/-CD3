import pandas as pd

# 🔥 1. Tạo dữ liệu cho từng sheet

# Sheet 1: Hàng hóa
hanghoa = pd.DataFrame({
    "MaSP": ["SP01","SP02","SP03"],
    "TenSP": ["Ao thun","Quan jean","Giay"],
    "SoLuong": [100, 50, 70]
})

# Sheet 2: Nhập kho
nhapkho = pd.DataFrame({
    "MaSP": ["SP01","SP02","SP03"],
    "SoLuongNhap": [20, 10, 15],
    "NgayNhap": ["2024-01-01","2024-01-02","2024-01-03"]
})

# Sheet 3: Xuất kho
xuatkho = pd.DataFrame({
    "MaSP": ["SP01","SP02","SP03"],
    "SoLuongXuat": [5, 8, 10],
    "NgayXuat": ["2024-01-05","2024-01-06","2024-01-07"]
})

# 🔥 2. Ghi vào 1 file Excel nhiều sheet
with pd.ExcelWriter("kho.xlsx") as writer:
    hanghoa.to_excel(writer, sheet_name="HangHoa", index=False)
    nhapkho.to_excel(writer, sheet_name="NhapKho", index=False)
    xuatkho.to_excel(writer, sheet_name="XuatKho", index=False)

print("✅ Đã tạo file kho.xlsx\n")

# 🔥 3. Đọc từng sheet
df_hh = pd.read_excel("kho.xlsx", sheet_name="HangHoa")
df_nk = pd.read_excel("kho.xlsx", sheet_name="NhapKho")
df_xk = pd.read_excel("kho.xlsx", sheet_name="XuatKho")

# 🔥 4. Kiểm tra cấu trúc
print("=== HangHoa ===")
print(df_hh.info())

print("\n=== NhapKho ===")
print(df_nk.info())

print("\n=== XuatKho ===")
print(df_xk.info())

# 🔥 5. Mô tả chức năng từng sheet
print("\n=== MÔ TẢ ===")
print("- HangHoa: Lưu thông tin sản phẩm và số lượng tồn kho")
print("- NhapKho: Lưu các lần nhập hàng vào kho")
print("- XuatKho: Lưu các lần xuất hàng khỏi kho")