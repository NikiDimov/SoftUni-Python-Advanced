N = int(input())
matrix = [[int(c) for c in input().split()] for r in range(N)]
bombs = input().split()
bombs_pos = []


def checker(x1, y1):
    if matrix[x1][y1] > 0:
        matrix[x1][y1] -= power


for bomb in bombs:
    x, y = bomb.split(',')
    bombs_pos.append((int(x), int(y)))
for x, y in bombs_pos:
    power = matrix[x][y]
    if power <= 0:
        continue
    matrix[x][y] = 0
    if x - 1 in range(0, N) and y in range(0, N):
        checker(x - 1, y)
    if x - 1 in range(0, N) and y + 1 in range(0, N):
        checker(x - 1, y + 1)
    if x in range(0, N) and y + 1 in range(0, N):
        checker(x, y + 1)
    if x + 1 in range(0, N) and y + 1 in range(0, N):
        checker(x + 1, y + 1)
    if x + 1 in range(0, N) and y in range(0, N):
        checker(x + 1, y)
    if x + 1 in range(0, N) and y - 1 in range(0, N):
        checker(x + 1, y - 1)
    if x in range(0, N) and y - 1 in range(0, N):
        checker(x, y - 1)
    if x - 1 in range(0, N) and y - 1 in range(0, N):
        checker(x - 1, y - 1)
alive_cells = [el for row in matrix for el in row if el > 0]
print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")
for row in matrix:
    print(*row)
