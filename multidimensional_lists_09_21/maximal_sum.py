row, column = [int(el) for el in input().split()]
matrix = [[int(c) for c in input().split()] for r in range(row)]
square_matrix = []
sum_of_square_matrix = 0
for r in range(row - 2):
    for c in range(column - 2):
        current_square_matrix = [[matrix[r][c], matrix[r][c + 1], matrix[r][c + 2]],
                                 [matrix[r + 1][c], matrix[r + 1][c + 1], matrix[r + 1][c + 2]],
                                 [matrix[r + 2][c], matrix[r + 2][c + 1], matrix[r + 2][c + 2]],
                                 ]
        flattened_matrix = [el for row in current_square_matrix for el in row]
        if sum(flattened_matrix) >= sum_of_square_matrix:
            sum_of_square_matrix = sum(flattened_matrix)
            square_matrix = current_square_matrix
print(f"Sum = {sum_of_square_matrix}")
for row in square_matrix:
    print(*row)

