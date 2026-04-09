import pandas as pd

print("=== Đọc file UTF-8 ===")
try:
    df_utf8 = pd.read_csv("sinhvien_utf8.csv", encoding="utf-8")
    print(df_utf8)
except Exception as e:
    print("Lỗi UTF-8:", e)

print("\n=== Đọc file ANSI ===")
try:
    df_ansi = pd.read_csv("sinhvien_ansi.csv", encoding="cp1258")
    print(df_ansi)
except Exception as e:
    print("Lỗi ANSI:", e)

# 🔥 Kết quả cần đạt
print("\n=== KẾT LUẬN ===")
print("- Nhận diện lỗi tiếng Việt khi bị sai encoding (ví dụ: Nguy?n, Tr?n)")
print("- Nguyên nhân: sai bảng mã giữa file và khi đọc")
print("- Cách xử lý: dùng encoding phù hợp (utf-8, cp1258)")
print("- Có thể thử nhiều encoding nếu chưa biết loại file")
print("- Đảm bảo dữ liệu hiển thị đúng tiếng Việt")