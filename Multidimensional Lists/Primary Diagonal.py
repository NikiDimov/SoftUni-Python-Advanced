rows = int(input())
matrix = []
sums = 0
for row in range(rows):
    matrix.append(list(map(int, input().split())))
for row in range(rows):
    sums += matrix[row][row]
print(sums)
