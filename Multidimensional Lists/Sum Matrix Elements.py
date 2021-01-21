rows, columns = input().split(", ")
rows = int(rows)
columns = int(columns)
matrix = []
sums = 0
for _ in range(rows):
    matrix.append([int(el)for el in input().split(", ")])
for mat in matrix:
    sums += sum(mat)
print(sums)
print(matrix)

