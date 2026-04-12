import pandas as pd

# 1. Đọc dữ liệu
df = pd.read_csv("muonsach.csv")

print("=== DỮ LIỆU BAN ĐẦU ===")
print(df)

# 2. Chuyển về kiểu datetime
df["NgayMuon"] = pd.to_datetime(df["NgayMuon"])
df["NgayTra"] = pd.to_datetime(df["NgayTra"], errors="coerce")

# 3. Chuẩn hóa TrangThai
df["TrangThai"] = df["TrangThai"].str.strip().str.lower()

df["TrangThai"] = df["TrangThai"].replace({
    "da tra": "DaTra",
    "đã trả": "DaTra",
    "datra": "DaTra",
    "chua tra": "ChuaTra",
    "chuatra": "ChuaTra"
})

# 4. Tính SoNgayMuon
# Nếu chưa trả thì dùng ngày hiện tại
today = pd.Timestamp.today()

df["SoNgayMuon"] = (df["NgayTra"].fillna(today) - df["NgayMuon"]).dt.days

# 5. Lọc sinh viên mượn quá 30 ngày (chưa trả)
qua_han = df[(df["NgayTra"].isna()) & (df["SoNgayMuon"] > 30)]

# 6. Xuất file
df.to_csv("muonsach_clean.csv", index=False)

print("\n=== SAU KHI XỬ LÝ ===")
print(df)

print("\n=== SINH VIÊN MƯỢN QUÁ 30 NGÀY ===")
print(qua_han)
