row, column = [int(el) for el in input().split()]
matrix = [[c for c in input().split()] for r in range(row)]
counter = 0

for r in range(row - 1):
    for c in range(column - 1):
        square_matrix = [[matrix[r][c], matrix[r][c + 1]], [matrix[r + 1][c], matrix[r + 1][c + 1]]]
        flattened_matrix = [el for row in square_matrix for el in row]
        if len(set(flattened_matrix)) == 1:
            counter += 1
print(counter)
