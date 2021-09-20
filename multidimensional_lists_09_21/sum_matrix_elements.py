rows, columns = [int(el) for el in input().split(", ")]
matrix = [[int(el) for el in input().split(", ")] for r in range(rows)]
sums = 0
for r in matrix:
    for el in r:
        sums += el
print(sums)
print(matrix)
