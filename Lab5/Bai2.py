import numpy as np

scores = np.array([
    [7.5, 8.0, 6.5, 9.0],
    [6.0, 7.0, 7.5, 8.0],
    [8.5, 9.0, 8.0, 9.5],
    [5.5, 6.0, 6.5, 7.0],
    [9.0, 8.5, 9.5, 8.0]
])

# Min-Max
min_col = np.min(scores, axis=0)
max_col = np.max(scores, axis=0)

denominator = max_col - min_col
denominator[denominator == 0] = 1

norm = (scores - min_col) / denominator
print("Chuẩn hóa [0,1]:\n", np.round(norm, 2))

# Z-score
mean_col = np.mean(scores, axis=0)
std_col = np.std(scores, axis=0)

std_col[std_col == 0] = 1

z_scores = (scores - mean_col) / std_col

print("Z-score:\n", np.round(z_scores, 2))
print("TB sau chuẩn hóa:", np.mean(z_scores, axis=0))
