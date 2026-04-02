import numpy as np

scores = np.array([
    [7.5, 8.0, 6.5, 9.0],
    [6.0, 7.0, 7.5, 8.0],
    [8.5, 9.0, 8.0, 9.5],
    [5.5, 6.0, 6.5, 7.0],
    [9.0, 8.5, 9.5, 8.0]
])

# 1. In ma trận
print("Ma trận điểm:\n", scores)

# 2. Trung bình toàn bộ
print("TB toàn bộ:", np.mean(scores))

# 3. TB từng sinh viên
avg_students = np.mean(scores, axis=1)
print("TB từng SV:", avg_students)

# 4. TB từng môn
print("TB từng môn:", np.mean(scores, axis=0))

# 5. Max - Min
print("Max:", np.max(scores))
print("Min:", np.min(scores))

# 6. Độ lệch chuẩn từng môn
print("Std từng môn:", np.std(scores, axis=0))

# 7. SV điểm cao nhất
best_student = np.argmax(avg_students)
print("SV giỏi nhất (index):", best_student)
