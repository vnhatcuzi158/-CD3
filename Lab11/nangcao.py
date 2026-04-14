import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score
from sklearn.metrics import confusion_matrix, classification_report

# ======================
# 1. Tạo dữ liệu
# ======================
data = {
    "X1": [1,2,3,4,5,6,7,8,9,10],
    "X2": [2,1,3,5,7,8,9,10,11,12],
    "X3": [5,3,6,2,7,9,4,8,10,11],
    "Y":  [2,4,5,4,5,7,8,9,10,12],
    "Label": [0,0,0,1,1,1,1,1,1,1]
}

df = pd.DataFrame(data)

# ======================
# Bài nâng cao 1: So sánh số biến
# ======================
print("\n=== Bài NC1 ===")

X1_only = df[["X1"]]
X_multi = df[["X1","X2","X3"]]
y = df["Y"]

X_train1, X_test1, y_train, y_test = train_test_split(X1_only, y, test_size=0.2, random_state=42)
X_train2, X_test2, _, _ = train_test_split(X_multi, y, test_size=0.2, random_state=42)

model1 = LinearRegression().fit(X_train1, y_train)
model2 = LinearRegression().fit(X_train2, y_train)

pred1 = model1.predict(X_test1)
pred2 = model2.predict(X_test2)

print("1 biến - MSE:", mean_squared_error(y_test, pred1))
print("Nhiều biến - MSE:", mean_squared_error(y_test, pred2))

# ======================
# Bài nâng cao 2: So sánh thực tế vs dự đoán
# ======================
print("\n=== Bài NC2 ===")

plt.plot(y_test.values, label="Thực tế", marker='o')
plt.plot(pred2, label="Dự đoán", marker='x')
plt.title("Thực tế vs Dự đoán")
plt.legend()
plt.show()

# ======================
# Bài nâng cao 3: Ma trận tương quan
# ======================
print("\n=== Bài NC3 ===")

corr = df.corr(numeric_only=True)
print(corr)

plt.imshow(corr, cmap="coolwarm")
plt.colorbar()
plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
plt.yticks(range(len(corr.columns)), corr.columns)
plt.title("Ma trận tương quan")
plt.show()

# ======================
# Bài nâng cao 4: So sánh 2 mô hình
# ======================
print("\n=== Bài NC4 ===")

X = df[["X1","X2"]]
y = df["Y"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

lr = LinearRegression().fit(X_train, y_train)
tree = DecisionTreeRegressor(random_state=42).fit(X_train, y_train)

pred_lr = lr.predict(X_test)
pred_tree = tree.predict(X_test)

print("Linear - MSE:", mean_squared_error(y_test, pred_lr))
print("Tree - MSE:", mean_squared_error(y_test, pred_tree))

print("Linear - R2:", r2_score(y_test, pred_lr))
print("Tree - R2:", r2_score(y_test, pred_tree))

# ======================
# Bài nâng cao 5: Chuẩn hóa
# ======================
print("\n=== Bài NC5 ===")

X = df[["X1","X2","X3"]]
y = df["Label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# chưa chuẩn hóa
model_raw = LogisticRegression(max_iter=1000).fit(X_train, y_train)
pred_raw = model_raw.predict(X_test)
print("Accuracy chưa chuẩn hóa:", accuracy_score(y_test, pred_raw))

# chuẩn hóa
scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

model_scaled = LogisticRegression(max_iter=1000).fit(X_train_s, y_train)
pred_scaled = model_scaled.predict(X_test_s)
print("Accuracy sau chuẩn hóa:", accuracy_score(y_test, pred_scaled))

# ======================
# Bài nâng cao 6: Confusion Matrix
# ======================
print("\n=== Bài NC6 ===")

model = LogisticRegression(max_iter=1000).fit(X_train, y_train)
y_pred = model.predict(X_test)

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))