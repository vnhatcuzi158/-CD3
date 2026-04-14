import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# ======================
# 1. Tạo dữ liệu
# ======================
data = {
    "Age": [18, 20, 22, 24, 26, 28, 30, 32, 34, 36],
    "StudyHours": [2, 3, 4, 5, 5, 6, 6, 7, 8, 9],
    "Score": [50, 55, 60, 65, 70, 75, 78, 82, 85, 90]
}

df = pd.DataFrame(data)

# ======================
# 2. Khám phá dữ liệu
# ======================
print("=== 5 dòng đầu ===")
print(df.head())

print("\n=== Thông tin dữ liệu ===")
print(df.info())

print("\n=== Thống kê mô tả ===")
print(df.describe())

# ======================
# 3. Vẽ biểu đồ
# ======================

# Histogram
df["Score"].plot(kind="hist", bins=5, title="Phân phối điểm")
plt.xlabel("Score")
plt.ylabel("Tần suất")
plt.show()

# Biểu đồ cột
group = df.groupby("Age")["Score"].mean()
group.plot(kind="bar", title="Điểm theo tuổi")
plt.xlabel("Age")
plt.ylabel("Score")
plt.show()

# Scatter plot
df.plot(kind="scatter", x="StudyHours", y="Score",
        title="Quan hệ giữa giờ học và điểm")
plt.show()

# ======================
# 4. Hồi quy tuyến tính
# ======================
X = df[["StudyHours"]]
y = df["Score"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("\n=== Kết quả mô hình ===")
print("MSE:", mean_squared_error(y_test, y_pred))
print("Hệ số:", model.coef_)
print("Intercept:", model.intercept_)

# So sánh kết quả
print("\n=== So sánh ===")
print(pd.DataFrame({"Thực tế": y_test, "Dự đoán": y_pred}))

# ======================
# 5. Xuất file CSV (nếu cần nộp)
# ======================
df.to_csv("data.csv", index=False)

print("\nĐã xuất file data.csv")