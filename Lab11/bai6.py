import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Tạo dữ liệu giả lập
data = {
    "X": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Y": [2, 4, 5, 4, 5, 7, 8, 9, 10, 12]
}

df = pd.DataFrame(data)

# Chọn biến
X = df[["X"]]
y = df["Y"]

# Chia train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Tạo và huấn luyện mô hình
model = LinearRegression()
model.fit(X_train, y_train)

# Dự đoán
y_pred = model.predict(X_test)

# Đánh giá
print("MSE:", mean_squared_error(y_test, y_pred))
print("Hệ số (coef):", model.coef_)
print("Intercept:", model.intercept_)