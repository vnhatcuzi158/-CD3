import pandas as pd
import matplotlib.pyplot as plt
import warnings

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Tắt warning
warnings.filterwarnings("ignore")

# ======================
# Bài 1: Tạo dữ liệu (FIX: 90 ngày)
# ======================
data = {
    "Date": pd.date_range(start="2024-01-01", periods=90, freq="D"),
    "Value": list(range(10, 100))[:90]  # dữ liệu tăng dần
}

df = pd.DataFrame(data)

df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")
df = df.set_index("Date")

print("=== Bài 1 ===")
print(df.head(10))

# ======================
# Bài 2: Theo tháng (FIX)
# ======================
print("\n=== Bài 2 ===")

monthly_data = df["Value"].resample("MS").sum()
print(monthly_data)

monthly_data.plot(figsize=(10,5), title="Tổng theo tháng")
plt.show()

# ======================
# Bài 3: Lag & MA
# ======================
print("\n=== Bài 3 ===")

df["Lag_1"] = df["Value"].shift(1)
df["MA_3"] = df["Value"].rolling(3).mean()
df["MA_7"] = df["Value"].rolling(7).mean()

print(df.head(10))

# ======================
# Bài 4: Hồi quy
# ======================
print("\n=== Bài 4 ===")

data_model = df.dropna()

X = data_model[["Lag_1", "MA_3", "MA_7"]]
y = data_model["Value"]

split = int(len(data_model)*0.8)

X_train = X.iloc[:split]
X_test = X.iloc[split:]
y_train = y.iloc[:split]
y_test = y.iloc[split:]

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("MSE:", mean_squared_error(y_test, y_pred))

# ======================
# Bài 5: KMeans
# ======================
print("\n=== Bài 5 ===")

df_cluster = pd.DataFrame({
    "Feature1": [1,2,3,8,9,10,15,16,17],
    "Feature2": [2,3,4,8,9,10,14,15,16]
})

scaler = StandardScaler()
X_scaled = scaler.fit_transform(df_cluster)

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df_cluster["Cluster"] = kmeans.fit_predict(X_scaled)

plt.scatter(df_cluster["Feature1"], df_cluster["Feature2"], c=df_cluster["Cluster"])
plt.title("KMeans Clustering")
plt.xlabel("Feature1")
plt.ylabel("Feature2")
plt.show()