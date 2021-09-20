row, column = [int(el)for el in input().split(", ")]
matrix = [[int(c)for c in input().split()]for r in range(row)]
for c in range(column):
    current_column = 0
    for r in range(row):
        current_column += matrix[r][c]
    print(current_column)


