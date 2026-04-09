import pandas as pd

# =========================
# 🔥 1. TẠO DỮ LIỆU MẪU
# =========================

# customers.csv
customers = pd.DataFrame({
    "makh": ["KH01","KH02","KH03"],
    "tenkh": ["Nguyen Van A","Tran Thi B","Le Van C"]
})
customers.to_csv("customers.csv", index=False)

# orders.xlsx
orders = pd.DataFrame({
    "madon": ["DH01","DH02","DH03","DH04"],
    "makh": ["KH01","KH02","KH01","KH03"],
    "masp": ["SP01","SP02","SP03","SP01"],
    "soluong": [2,1,3,1]
})
orders.to_excel("orders.xlsx", index=False)

# products.json
products = pd.DataFrame({
    "masp": ["SP01","SP02","SP03"],
    "tensp": ["Ao thun","Quan jean","Giay"],
    "nhom": ["Thoi trang","Thoi trang","Giay dep"],
    "gia": [150000,350000,500000]
})
products.to_json("products.json", orient="records")

print("✅ Đã tạo dữ liệu mẫu\n")

# =========================
# 🔥 2. ĐỌC DỮ LIỆU
# =========================
df_customers = pd.read_csv("customers.csv")
df_orders = pd.read_excel("orders.xlsx")
df_products = pd.read_json("products.json")

# =========================
# 🔥 3. LÀM SẠCH DỮ LIỆU
# =========================

# Chuẩn hóa tên cột (viết hoa chữ cái đầu)
df_customers.columns = ["MaKH","TenKH"]
df_orders.columns = ["MaDon","MaKH","MaSP","SoLuong"]
df_products.columns = ["MaSP","TenSP","Nhom","Gia"]

# Ép kiểu số
df_orders["SoLuong"] = df_orders["SoLuong"].astype(int)
df_products["Gia"] = df_products["Gia"].astype(float)

# =========================
# 🔥 4. GHÉP DỮ LIỆU
# =========================

# orders + customers
df_merge1 = pd.merge(df_orders, df_customers, on="MaKH")

# + products
df_full = pd.merge(df_merge1, df_products, on="MaSP")

# Tính tiền
df_full["ThanhTien"] = df_full["SoLuong"] * df_full["Gia"]

# =========================
# 🔥 5. BÁO CÁO
# =========================

# 📊 Báo cáo khách hàng
baocao_kh = df_full.groupby(["MaKH","TenKH"]).agg(
    SoDon=("MaDon", "count"),
    TongTien=("ThanhTien", "sum")
).reset_index()

# 📊 Báo cáo sản phẩm
baocao_sp = df_full.groupby("Nhom").agg(
    TongTien=("ThanhTien", "sum")
).reset_index()

print("=== Báo cáo khách hàng ===")
print(baocao_kh)

print("\n=== Báo cáo sản phẩm ===")
print(baocao_sp)

# =========================
# 🔥 6. XUẤT EXCEL NHIỀU SHEET
# =========================

with pd.ExcelWriter("baocao_tonghop.xlsx") as writer:
    baocao_kh.to_excel(writer, sheet_name="BaoCaoKhachHang", index=False)
    baocao_sp.to_excel(writer, sheet_name="BaoCaoSanPham", index=False)

print("\n✅ Đã xuất file baocao_tonghop.xlsx")