import csv

# Danh sách hợp lệ và lỗi
ds_hop_le = []
ds_loi = []

# Đọc file CSV
with open("diemlop.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:
        ma = row["MaSV"]
        ten = row["HoTen"]
        diem_str = row["Diem"]

        try:
            diem = float(diem_str)

            # Kiểm tra khoảng điểm
            if 0 <= diem <= 10:
                ds_hop_le.append((ma, ten, diem))
            else:
                ds_loi.append(f"{ma},{ten},{diem} -> Điểm ngoài khoảng")

        except ValueError:
            ds_loi.append(f"{ma},{ten},{diem_str} -> Không phải số")

# Tính điểm trung bình
if ds_hop_le:
    diem_tb = sum(sv[2] for sv in ds_hop_le) / len(ds_hop_le)
else:
    diem_tb = 0

# In kết quả
print("=== DỮ LIỆU HỢP LỆ ===")
for sv in ds_hop_le:
    print(f"{sv[0]} - {sv[1]} - {sv[2]}")

print(f"\nĐiểm trung bình (hợp lệ): {diem_tb:.2f}")

# Ghi file lỗi
with open("loi.txt", "w", encoding="utf-8") as f:
    f.write("=== DANH SÁCH LỖI ===\n")
    for loi in ds_loi:
        f.write(loi + "\n")

print("\nĐã ghi các dòng lỗi vào file loi.txt")
