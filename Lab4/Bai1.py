import numpy as np

# 1. Tạo dữ liệu
scores = np.array([
    [8.0, 7.5, 8.5, 7.0],
    [6.5, 6.0, 7.0, 6.5],
    [9.0, 8.5, 9.0, 8.5],
    [5.0, 5.5, 6.0, 5.5],
    [7.5, 7.0, 8.0, 7.5],
    [4.5, 5.0, 5.5, 5.0],
    [8.5, 9.0, 8.0, 9.0],
    [6.0, 6.5, 6.0, 6.5],
    [7.0, 7.5, 7.0, 8.0],
    [9.5, 9.0, 9.5, 9.0]
])

weights = np.array([0.1, 0.2, 0.3, 0.4])

# 1. Thông tin mảng
print("=== THÔNG TIN DỮ LIỆU ===")
print("Shape:", scores.shape)
print("Số chiều:", scores.ndim)
print("Kiểu dữ liệu:", scores.dtype)

# 2. Tính điểm tổng kết
final_score = scores @ weights
print("\n=== ĐIỂM TỔNG KẾT ===")
print(final_score)

# 3. Xếp loại
def classify(score):
    if score >= 8:
        return "A"
    elif score >= 6.5:
        return "B"
    elif score >= 5:
        return "C"
    else:
        return "D"

rank = np.array([classify(s) for s in final_score])
print("\n=== XẾP LOẠI ===")
print(rank)

# 4. Cao nhất - thấp nhất
max_idx = np.argmax(final_score)
min_idx = np.argmin(final_score)
print("\n=== MAX / MIN ===")
print("SV cao nhất:", max_idx, "Điểm:", final_score[max_idx])
print("SV thấp nhất:", min_idx, "Điểm:", final_score[min_idx])

# 5. SV >= 7.0
good_students = np.where(final_score >= 7.0)[0]
print("\n=== SV >= 7.0 ===")
print(good_students)

# 6. SV có điểm < 5
low_component = np.any(scores < 5.0, axis=1)
print("\n=== SV có điểm thành phần < 5 ===")
print(np.where(low_component)[0])

# 7. Top 3
rank_idx = np.argsort(final_score)[::-1]
top3 = rank_idx[:3]
print("\n=== TOP 3 SINH VIÊN ===")
print("Vị trí:", top3)
print("Điểm:", final_score[top3])

# 8. Z-score cuối kỳ
final_exam = scores[:, 3]
z_score = (final_exam - final_exam.mean()) / final_exam.std()
print("\n=== Z-SCORE CUỐI KỲ ===")
print(z_score)

# Nhận xét
print("\n=== NHẬN XÉT ===")
print("- Lớp có nhiều sinh viên đạt loại khá và giỏi.")
print("- Một số sinh viên có điểm thành phần dưới 5 cần cải thiện.")
print("- Điểm cuối kỳ có sự phân hóa nhưng không quá lớn.")
