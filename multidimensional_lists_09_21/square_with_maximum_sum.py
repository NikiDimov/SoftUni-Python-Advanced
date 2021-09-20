rows, columns = [int(el) for el in input().split(', ')]
matrix = [[int(c)for c in input().split(', ')]for r in range(rows)]
sub_matrix = []
sub_matrix_sum = 0
for r in range(rows-1):
    for c in range(columns-1):
        current_sub_matrix = [[matrix[r][c], matrix[r][c+1]], [matrix[r+1][c], matrix[r+1][c+1]]]
        current_matrix_sum = sum([c for row in current_sub_matrix for c in row])
        if current_matrix_sum > sub_matrix_sum:
            sub_matrix_sum = current_matrix_sum
            sub_matrix = current_sub_matrix
for r in sub_matrix:
    print(*r)
print(sub_matrix_sum)
