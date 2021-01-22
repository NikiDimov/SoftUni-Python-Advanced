rows, columns = input().split(", ")
rows = int(rows)
columns = int(columns)
matrix = []
for row in range(rows):
    matrix.append(list(map(int, input().split())))
for column in range(columns):
    sum_col = 0
    for row in range(rows):
        sum_col += matrix[row][column]
    print(sum_col)
    