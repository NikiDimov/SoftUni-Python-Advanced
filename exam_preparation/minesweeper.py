import re
N = int(input())
bombs = int(input())
matrix = [[0 for c in range(N)] for r in range(N)]
for i in range(bombs):
    bomb = input()
    pattern = r"\d+"
    match = re.findall(pattern, bomb)
    row_bomb, col_bomb = int(match[0]), int(match[1])
    matrix[row_bomb][col_bomb] = "*"

for row in range(N):
    for col in range(N):
        if matrix[row][col] != "*":
            sum_of_bombs = 0
            if 0 <= row - 1 < N and matrix[row - 1][col] == "*":
                sum_of_bombs += 1
            if 0 <= row + 1 < N and matrix[row + 1][col] == "*":
                sum_of_bombs += 1
            if 0 <= col + 1 < N and matrix[row][col + 1] == "*":
                sum_of_bombs += 1
            if 0 <= col - 1 < N and matrix[row][col - 1] == "*":
                sum_of_bombs += 1
            if 0 <= col - 1 < N and 0 <= row - 1 < N and matrix[row - 1][col - 1] == "*":
                sum_of_bombs += 1
            if 0 <= col + 1 < N and 0 <= row - 1 < N and matrix[row - 1][col + 1] == "*":
                sum_of_bombs += 1
            if 0 <= col - 1 < N and 0 <= row + 1 < N and matrix[row + 1][col - 1] == "*":
                sum_of_bombs += 1
            if 0 <= col + 1 < N and 0 <= row + 1 < N and matrix[row + 1][col + 1] == "*":
                sum_of_bombs += 1
            matrix[row][col] = sum_of_bombs
print(*[' '.join(map(str, row)) for row in matrix], sep="\n")
