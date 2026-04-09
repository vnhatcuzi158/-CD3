import pandas as pd

# 🔥 1. Tạo file students.csv
students = pd.DataFrame({
    "MaSV": ["SV001","SV002","SV003","SV004"],
    "HoTen": ["Nguyen Van A","Tran Thi B","Le Van C","Pham Thi D"],
    "Lop": ["CTK42","CTK42","CTK43","CTK43"]
})
students.to_csv("students.csv", index=False)

# 🔥 2. Tạo file scores.xlsx
scores = pd.DataFrame({
    "MaSV": ["SV001","SV002","SV003","SV004"],
    "DiemQT": [8.0,7.0,6.5,9.0],
    "DiemThi": [7.5,8.0,6.0,8.5]
})
scores.to_excel("scores.xlsx", index=False)

print("✅ Đã tạo students.csv và scores.xlsx\n")

# 🔥 3. Đọc dữ liệu
df_students = pd.read_csv("students.csv")
df_scores = pd.read_excel("scores.xlsx")

# 🔥 4. Ghép dữ liệu theo MaSV
df_merge = pd.merge(df_students, df_scores, on="MaSV")

# 🔥 5. Tính điểm tổng kết
df_merge["DiemTK"] = (df_merge["DiemQT"] + df_merge["DiemThi"]) / 2

# 🔥 6. Chọn cột cần thiết
df_final = df_merge[["MaSV","HoTen","Lop","DiemQT","DiemThi","DiemTK"]]

print("=== BẢNG TỔNG HỢP ===")
print(df_final)

# 🔥 7. Xuất ra Excel
df_final.to_excel("tonghop_diem.xlsx", index=False)

print("\n✅ Đã lưu file tonghop_diem.xlsx")