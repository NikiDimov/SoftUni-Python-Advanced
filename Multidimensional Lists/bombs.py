n = int(input())
matrix = []
for _ in range(n):
    matrix.append([int(el) for el in input().split()])
bombs = input().split()
for bomb in bombs:
    row_bomb, col_bomb = map(int, bomb.split(","))
    explosion = matrix[row_bomb][col_bomb]
    if explosion <= 0:
        continue
    matrix[row_bomb][col_bomb] = 0
    if 0 <= row_bomb - 1 < n and 0 <= col_bomb - 1 < n and matrix[row_bomb - 1][col_bomb - 1] > 0:
        matrix[row_bomb - 1][col_bomb - 1] -= explosion
    if 0 <= row_bomb - 1 < n and matrix[row_bomb - 1][col_bomb] > 0:
        matrix[row_bomb - 1][col_bomb] -= explosion
    if 0 <= row_bomb - 1 < n and 0 <= col_bomb + 1 < n and matrix[row_bomb - 1][col_bomb + 1] > 0:
        matrix[row_bomb - 1][col_bomb + 1] -= explosion
    if 0 <= col_bomb + 1 < n and matrix[row_bomb][col_bomb + 1] > 0:
        matrix[row_bomb][col_bomb + 1] -= explosion
    if 0 <= col_bomb + 1 < n and 0 <= row_bomb + 1 < n and matrix[row_bomb + 1][col_bomb + 1] > 0:
        matrix[row_bomb + 1][col_bomb + 1] -= explosion
    if 0 <= row_bomb + 1 < n and matrix[row_bomb + 1][col_bomb] > 0:
        matrix[row_bomb + 1][col_bomb] -= explosion
    if 0 <= row_bomb + 1 < n and 0 <= col_bomb - 1 < n and matrix[row_bomb + 1][col_bomb - 1] > 0:
        matrix[row_bomb + 1][col_bomb - 1] -= explosion
    if 0 <= col_bomb - 1 < n and matrix[row_bomb][col_bomb - 1] > 0:
        matrix[row_bomb][col_bomb - 1] -= explosion
counter = 0
sums = 0
for r in range(n):
    for c in range(n):
        if matrix[r][c] > 0:
            counter += 1
            sums += matrix[r][c]

print(f"Alive cells: {counter}")
print(f"Sum: {sums}")
for r in matrix:
    print(" ".join(map(str, r)))
