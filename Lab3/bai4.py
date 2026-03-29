# Hàm nhập danh sách sinh viên
def nhap_danh_sach():
    ds = []
    n = int(input("Nhập số lượng sinh viên: "))

    for i in range(n):
        print(f"\nNhập sinh viên thứ {i+1}:")
        ma = input("Mã SV: ")
        ten = input("Họ tên: ")
        diem = float(input("Điểm: "))
        ds.append((ma, ten, diem))

    return ds


# Hàm tính điểm trung bình
def tinh_diem_trung_binh(ds):
    tong = sum(sv[2] for sv in ds)
    return tong / len(ds) if ds else 0


# Hàm tìm sinh viên điểm cao nhất
def tim_sv_max(ds):
    return max(ds, key=lambda sv: sv[2])


# Hàm xếp loại
def xep_loai(diem):
    if diem >= 8:
        return "A"
    elif diem >= 6.5:
        return "B"
    elif diem >= 5:
        return "C"
    else:
        return "F"


# Hàm in báo cáo
def in_bao_cao(ds):
    print("\n===== BÁO CÁO SINH VIÊN =====")

    for sv in ds:
        loai = xep_loai(sv[2])
        print(f"Mã: {sv[0]}, Tên: {sv[1]}, Điểm: {sv[2]}, Xếp loại: {loai}")

    # Điểm trung bình
    dtb = tinh_diem_trung_binh(ds)
    print(f"\nĐiểm trung bình lớp: {dtb:.2f}")

    # Sinh viên cao nhất
    sv_max = tim_sv_max(ds)
    print("\nSinh viên điểm cao nhất:")
    print(f"Mã: {sv_max[0]}, Tên: {sv_max[1]}, Điểm: {sv_max[2]}")


# ===== Chương trình chính =====
def main():
    ds = nhap_danh_sach()
    in_bao_cao(ds)


# Chạy chương trình
if __name__ == "__main__":
    main()
