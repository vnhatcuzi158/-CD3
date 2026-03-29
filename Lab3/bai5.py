# Hàm đọc file và chuyển thành danh sách sinh viên
def doc_file(filename):
    ds = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line == "":
                continue
            parts = line.split(",")
            ma = parts[0]
            ten = parts[1]
            diem = float(parts[2])
            ds.append((ma, ten, diem))
    return ds


# Hàm thống kê
def thong_ke(ds):
    tong_sv = len(ds)
    tong_diem = sum(sv[2] for sv in ds)
    diem_tb = tong_diem / tong_sv if tong_sv > 0 else 0

    dat = sum(1 for sv in ds if sv[2] >= 5)
    khong_dat = tong_sv - dat

    return tong_sv, diem_tb, dat, khong_dat


# Hàm ghi báo cáo
def ghi_file(filename, tong_sv, diem_tb, dat, khong_dat):
    with open(filename, "w", encoding="utf-8") as f:
        f.write("===== BAO CAO SINH VIEN =====\n")
        f.write(f"Tong so sinh vien: {tong_sv}\n")
        f.write(f"Diem trung binh: {diem_tb:.2f}\n")
        f.write(f"So sinh vien dat (>=5): {dat}\n")
        f.write(f"So sinh vien khong dat (<5): {khong_dat}\n")


# ===== Chương trình chính =====
def main():
    ds = doc_file("sinhvien.txt")

    tong_sv, diem_tb, dat, khong_dat = thong_ke(ds)

    print("Đã đọc dữ liệu thành công!")
    print(f"Tổng SV: {tong_sv}")
    print(f"Điểm TB: {diem_tb:.2f}")
    print(f"Số SV đạt: {dat}")
    print(f"Số SV không đạt: {khong_dat}")

    ghi_file("baocao.txt", tong_sv, diem_tb, dat, khong_dat)
    print("Đã ghi báo cáo vào file baocao.txt")


# Chạy chương trình
if __name__ == "__main__":
    main()
