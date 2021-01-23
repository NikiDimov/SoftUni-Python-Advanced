rows, cols = [int(el) for el in input().split()]


def init_matrix():
    mat = []
    for _ in range(rows):
        mat.append(input().split())
    return mat


def check_elements_are_equal(row, col, matr):
    if matr[row][col] == matr[row][col + 1] == matr[row + 1][col] == matr[row + 1][col + 1]:
        return True
    return False


matrix = init_matrix()
counter = 0

for row_index in range(rows - 1):
    for col_index in range(cols - 1):
        if check_elements_are_equal(row_index, col_index, matrix):
            counter += 1

print(counter)
