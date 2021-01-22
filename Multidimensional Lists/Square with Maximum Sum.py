rows, columns = input().split(", ")
rows = int(rows)
columns = int(columns)
matrix = []
result = []
sums = 0
current_sums = 0
for row in range(rows):
    matrix.append([int(el) for el in input().split(", ")])
for row in range(rows - 1):
    for column in range(columns - 1):
        small_matrix = [[matrix[row][column], matrix[row][column + 1]],
                        [matrix[row + 1][column], matrix[row + 1][column + 1]]]
        current_sums = sum(small_matrix[0]) + sum(small_matrix[1])
        if current_sums > sums:
            result = small_matrix
            sums = current_sums
for x, y in result:
    print(x, y)
print(sums)
