import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Tạo dữ liệu giả lập (có nhãn Label)
data = {
    "X1": [1, 2, 3, 4, 5, 6, 7, 8],
    "X2": [2, 1, 3, 5, 7, 8, 9, 10],
    "Label": [0, 0, 0, 1, 1, 1, 1, 1]  # 0: thấp, 1: cao (ví dụ)
}

df = pd.DataFrame(data)

# Chọn biến đầu vào và nhãn
X = df[["X1", "X2"]]
y = df["Label"]

# Chia train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Tạo và huấn luyện mô hình
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Dự đoán
y_pred = model.predict(X_test)

# Đánh giá
print("Accuracy:", accuracy_score(y_test, y_pred))