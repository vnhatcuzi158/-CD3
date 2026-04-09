import pandas as pd

print("=== Đọc SAI (mặc định sep=',') ===")
df_sai = pd.read_csv("sales_semicolon.csv")
print(df_sai.head())

print("\n=== Đọc ĐÚNG (sep=';') ===")
df_dung = pd.read_csv("sales_semicolon.csv", sep=';')
print(df_dung.head())