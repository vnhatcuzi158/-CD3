# Dữ liệu mẫu
subjects = ["Python", "CSDL", "Python", "Java", "CSDL", "AI", "Python"]

# 1. Loại bỏ phần tử trùng lặp bằng set
unique_subjects = set(subjects)
print("Danh sách môn học (không trùng):")
print(unique_subjects)

# 2. Đếm số lần xuất hiện bằng dict
count_dict = {}

for subject in subjects:
    if subject in count_dict:
        count_dict[subject] += 1
    else:
        count_dict[subject] = 1

print("\nSố lần xuất hiện của từng môn:")
for k, v in count_dict.items():
    print(f"{k}: {v}")

# 3. Tìm môn học được đăng ký nhiều nhất
max_subject = None
max_count = 0

for subject, count in count_dict.items():
    if count > max_count:
        max_count = count
        max_subject = subject

print(f"\nMôn học đăng ký nhiều nhất: {max_subject} ({max_count} lần)")

# 4. Sắp xếp theo số lần giảm dần
sorted_subjects = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)

print("\nDanh sách sau khi sắp xếp giảm dần:")
for subject, count in sorted_subjects:
    print(f"{subject}: {count}")
