rows, cols = [int(el) for el in input().split()]


def init_matrix():
    mat = []
    for _ in range(rows):
        mat.append([int(el) for el in input().split()])
    return mat


def init_small_matrix(row, col, matrix):
    small_matrix = [[matrix[row][col], matrix[row][col + 1], matrix[row][col + 2]],
                    [matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2]],
                    [matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]],
                    ]
    return small_matrix


matrix = init_matrix()
dict_matrices = {}
for row in range(rows - 2):
    for col in range(cols - 2):
        small = init_small_matrix(row, col, matrix)
        current_sums = sum(small[0]) + sum(small[1]) + sum(small[2])
        if current_sums not in dict_matrices:
            dict_matrices[current_sums] = small

print(f"Sum = {max(dict_matrices)}")
for el in dict_matrices[max(dict_matrices)]:
    print(" ".join(map(str, el)))


