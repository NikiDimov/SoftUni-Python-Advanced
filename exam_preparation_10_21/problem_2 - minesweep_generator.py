N = int(input())
matrix = [list('-' * N) for row in range(N)]
bombs = int(input())


def checker(x, y):
    global counter
    if x in range(0, N) and y in range(0, N):
        if matrix[x][y] == '*':
            counter += 1


for _ in range(bombs):
    bomb = eval(input())
    matrix[bomb[0]][bomb[1]] = '*'
for r in range(N):
    for c in range(N):
        if matrix[r][c] == '-':
            counter = 0
            checker(r, c - 1)
            checker(r - 1, c - 1)
            checker(r - 1, c)
            checker(r - 1, c + 1)
            checker(r, c + 1)
            checker(r + 1, c + 1)
            checker(r + 1, c)
            checker(r + 1, c - 1)
            matrix[r][c] = counter

for row in matrix:
    print(*row)
