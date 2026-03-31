import numpy as np

# 1. Dữ liệu chuyên cần
attendance = np.array([
    [1,1,1,1,1,1,1,1],
    [1,1,0,1,1,0,1,1],
    [1,0,0,1,1,1,0,1],
    [1,1,1,1,0,1,1,1],
    [0,1,1,0,1,1,1,0],
    [1,1,1,1,1,1,0,1],
    [1,0,1,0,1,0,1,0],
    [1,1,1,1,1,1,1,0],
    [0,0,1,1,0,1,1,1],
    [1,1,1,0,1,1,1,1],
    [1,1,0,0,1,0,1,1],
    [1,1,1,1,1,0,1,1]
])

print("=== MA TRẬN CHUYÊN CẦN ===")
print(attendance)

# 1. Tổng số buổi đi học
present_count = attendance.sum(axis=1)
print("\n=== SỐ BUỔI CÓ MẶT ===")
print(present_count)

# 2. Tỉ lệ chuyên cần (%)
rate = present_count / attendance.shape[1] * 100
print("\n=== TỈ LỆ CHUYÊN CẦN (%) ===")
print(rate)

# 3. Sinh viên bị cảnh báo (<75%)
warning_idx = np.where(rate < 75)[0]
print("\n=== SINH VIÊN BỊ CẢNH BÁO ===")
print(warning_idx)

# 4. Buổi học vắng nhiều nhất
absent_count_by_session = (attendance == 0).sum(axis=0)
worst_session = np.argmax(absent_count_by_session)
print("\n=== BUỔI VẮNG NHIỀU NHẤT ===")
print("Buổi:", worst_session)
print("Số SV vắng:", absent_count_by_session[worst_session])

# 5. SV đi học đầy đủ
full_attendance = np.where(np.all(attendance == 1, axis=1))[0]
print("\n=== SV ĐI HỌC ĐẦY ĐỦ ===")
print(full_attendance)

# 6. SV vắng 2 buổi liên tiếp
two_absent_in_row = np.where(
    np.any((attendance[:, :-1] == 0) & (attendance[:, 1:] == 0), axis=1)
)[0]

print("\n=== SV VẮNG 2 BUỔI LIÊN TIẾP ===")
print(two_absent_in_row)

# 7. Nhận xét
print("\n=== NHẬN XÉT ===")
print("- Phần lớn sinh viên có ý thức đi học khá tốt.")
print("- Một số sinh viên có tỉ lệ chuyên cần thấp (<75%) cần được cảnh báo.")
print("- Có sinh viên vắng nhiều buổi liên tiếp, thể hiện ý thức học tập chưa cao.")
print("- Một số sinh viên đi học đầy đủ, thể hiện tinh thần học tập nghiêm túc.")
