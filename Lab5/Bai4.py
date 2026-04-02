import numpy as np

# ======================
# 1. Tạo ma trận
# ======================
A = np.array([[2, 1],
              [1, 3]])
B = np.array([[4, 2],
              [1, 5]])

# ======================
# 2. Cộng, trừ, nhân ma trận
# ======================
print("A + B =\n", A + B)
print("A - B =\n", A - B)
print("A @ B =\n", A @ B)  # nhân ma trận chuẩn

# ======================
# 3. Định thức & kiểm tra khả nghịch
# ======================
det_A = np.linalg.det(A)
print("det(A) =", det_A)

if det_A != 0:
    inv_A = np.linalg.inv(A)
    print("A^-1 =\n", inv_A)
else:
    print("Ma trận A không khả nghịch!")

# ======================
# 4. Giải hệ phương trình
# Hệ: 2x + y = 5, x + 3y = 7
# ======================
b = np.array([5, 7])

try:
    solution = np.linalg.solve(A, b)
    print("Nghiệm hệ phương trình:", solution)
except np.linalg.LinAlgError:
    print("Hệ phương trình không có nghiệm hoặc vô số nghiệm")
