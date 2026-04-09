import pandas as pd
import os

# 🔥 1. Hàm load dữ liệu tổng quát
def load_data(file_path):
    try:
        ext = os.path.splitext(file_path)[1].lower()

        if ext == ".csv":
            df = pd.read_csv(file_path)
        elif ext == ".xlsx":
            df = pd.read_excel(file_path)
        elif ext == ".json":
            df = pd.read_json(file_path)
        else:
            raise ValueError("❌ Định dạng file không hỗ trợ!")

        print(f"✅ Đã đọc file: {file_path}")
        return df

    except Exception as e:
        print(f"Lỗi khi đọc {file_path}: {e}")
        return None


# 🔥 2. Tạo dữ liệu mẫu để test

# CSV
df_csv = pd.DataFrame({
    "Ma": ["A1", "A2"],
    "GiaTri": [100, 200]
})
df_csv.to_csv("test.csv", index=False)

# Excel
df_excel = pd.DataFrame({
    "Ma": ["B1", "B2"],
    "GiaTri": [300, 400]
})
df_excel.to_excel("test.xlsx", index=False)

# JSON
df_json = pd.DataFrame({
    "Ma": ["C1", "C2"],
    "GiaTri": [500, 600]
})
df_json.to_json("test.json", orient="records")

print("✅ Đã tạo 3 file test\n")

# 🔥 3. Kiểm thử hàm

files = ["test.csv", "test.xlsx", "test.json", "test.txt"]

for f in files:
    print(f"\n--- Đang đọc: {f} ---")
    df = load_data(f)
    
    if df is not None:
        print(df.head())