import pandas as pd
import re

# 1. Đọc dữ liệu
df = pd.read_csv("reviews.csv")

print("=== BAN ĐẦU ===")
print(df)

# =========================
# 2. XÓA TRÙNG
# =========================
df = df.drop_duplicates()

# =========================
# 3. XỬ LÝ RATING (1–5)
# =========================
df["Rating"] = pd.to_numeric(df["Rating"], errors="coerce")

# thay rating sai bằng median
median_rating = df[(df["Rating"] >= 1) & (df["Rating"] <= 5)]["Rating"].median()

df["Rating"] = df["Rating"].apply(
    lambda x: x if 1 <= x <= 5 else median_rating
)

# =========================
# 4. LÀM SẠCH COMMENT
# =========================

def clean_text(text):
    text = str(text).strip()
    
    # xóa ký tự lặp (vd: deppppp → dep)
    text = re.sub(r'(.)\1+', r'\1', text)
    
    return text

df["Comment"] = df["Comment"].apply(clean_text)

# =========================
# 5. ĐỘ DÀI COMMENT
# =========================
df["DoDaiComment"] = df["Comment"].str.len()

# =========================
# 6. CHUẨN HÓA DANH MỤC
# =========================
df["ProductCategory"] = df["ProductCategory"].str.strip().str.lower().str.title()

# =========================
# 7. THỐNG KÊ
# =========================
thong_ke = df.groupby("ProductCategory")["Rating"].mean()

# =========================
# 8. XUẤT FILE
# =========================
df.to_csv("reviews_clean.csv", index=False)
thong_ke.to_csv("reviews_thongke.csv")

print("\n=== SAU XỬ LÝ ===")
print(df)

print("\n=== ĐIỂM TRUNG BÌNH ===")
print(thong_ke)