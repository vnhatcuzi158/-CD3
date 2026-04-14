import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# ======================
# Tạo dữ liệu
# ======================
data = {
    "Date": pd.date_range(start="2024-01-01", periods=90, freq="D"),
    "Value": list(range(10, 100))[:90]
}

df = pd.DataFrame(data)
df["Date"] = pd.to_datetime(df["Date"])
df = df.set_index("Date")

# ======================
# Tạo đặc trưng
# ======================
df["Lag_1"] = df["Value"].shift(1)
df["MA_3"] = df["Value"].rolling(3).mean()
df["MA_5"] = df["Value"].rolling(5).mean()
df["MA_7"] = df["Value"].rolling(7).mean()
df["MA_14"] = df["Value"].rolling(14).mean()

data_model = df.dropna()

# ======================
# NC1: So sánh MA
# ======================
print("=== NC1 ===")

feature_sets = {
    "MA_3": ["Lag_1", "MA_3"],
    "MA_5": ["Lag_1", "MA_5"],
    "MA_7": ["Lag_1", "MA_7"],
    "MA_14": ["Lag_1", "MA_14"]
}

for name, features in feature_sets.items():
    X = data_model[features]
    y = data_model["Value"]

    split = int(len(data_model)*0.8)
    X_train, X_test = X.iloc[:split], X.iloc[split:]
    y_train, y_test = y.iloc[:split], y.iloc[split:]

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    print(name, "MSE =", mean_squared_error(y_test, y_pred))

# ======================
# NC2: Dự báo 5 bước (FIX)
# ======================
print("\n=== NC2: Dự báo 5 bước ===")

# train lại model
model = LinearRegression()
X = data_model[["Lag_1", "MA_3"]]
y = data_model["Value"]
model.fit(X, y)

last_value = data_model["Value"].iloc[-1]
future_preds = []

for i in range(5):
    # FIX: dùng DataFrame có tên cột
    input_data = pd.DataFrame([[last_value, last_value]],
                              columns=["Lag_1", "MA_3"])
    
    pred = model.predict(input_data)[0]
    future_preds.append(pred)
    last_value = pred

for i, val in enumerate(future_preds, 1):
    print(f"Bước {i}: {val}")

# ======================
# NC3: Vẽ thực tế vs dự đoán
# ======================
print("\n=== NC3 ===")

X = data_model[["Lag_1", "MA_3"]]
y = data_model["Value"]

split = int(len(data_model)*0.8)
X_train, X_test = X.iloc[:split], X.iloc[split:]
y_train, y_test = y.iloc[:split], y.iloc[split:]

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

plt.figure(figsize=(10,5))
plt.plot(y_test.index, y_test.values, label="Thực tế")
plt.plot(y_test.index, y_pred, label="Dự đoán")
plt.title("So sánh thực tế và dự đoán")
plt.legend()
plt.show()

# ======================
# NC4: Xu hướng
# ======================
print("\n=== NC4 ===")

trend_data = df.dropna().copy()
trend_data["TimeIndex"] = np.arange(len(trend_data))

X = trend_data[["TimeIndex"]]
y = trend_data["Value"]

model = LinearRegression()
model.fit(X, y)

trend_data["Trend"] = model.predict(X)

plt.figure(figsize=(10,5))
plt.plot(trend_data.index, trend_data["Value"], label="Giá trị gốc")
plt.plot(trend_data.index, trend_data["Trend"], label="Xu hướng")
plt.title("Phân tích xu hướng")
plt.legend()
plt.show()