def position(m, n, pos=[]):
    for r in range(n):
        if not pos:
            for c in range(n):
                if m[r][c] == "P":
                    pos = [r, c]
                    return pos


initial_string = input()
N = int(input())
matrix = [list(input()) for _ in range(N)]
current_position = position(matrix, N)
M = int(input())
for _ in range(M):
    command = input()
    if command == "down":
        if 0 <= current_position[0] + 1 < N:
            matrix[current_position[0]][current_position[1]] = "-"
            current_position[0] += 1
            if not matrix[current_position[0]][current_position[1]] == "-":
                initial_string += matrix[current_position[0]][current_position[1]]
                matrix[current_position[0]][current_position[1]] = "P"
        else:
            initial_string = initial_string[:-1]
    elif command == "right":
        if 0 <= current_position[1] + 1 < N:
            matrix[current_position[0]][current_position[1]] = "-"
            current_position[1] += 1
            if not matrix[current_position[0]][current_position[1]] == "-":
                initial_string += matrix[current_position[0]][current_position[1]]
                matrix[current_position[0]][current_position[1]] = "P"
        else:
            initial_string = initial_string[:-1]
    elif command == "up":
        if 0 <= current_position[0] - 1 < N:
            matrix[current_position[0]][current_position[1]] = "-"
            current_position[0] -= 1
            if not matrix[current_position[0]][current_position[1]] == "-":
                initial_string += matrix[current_position[0]][current_position[1]]
                matrix[current_position[0]][current_position[1]] = "P"
        else:
            initial_string = initial_string[:-1]
    elif command == "left":
        if 0 <= current_position[1] - 1 < N:
            matrix[current_position[0]][current_position[1]] = "-"
            current_position[1] -= 1
            if not matrix[current_position[0]][current_position[1]] == "-":
                initial_string += matrix[current_position[0]][current_position[1]]
                matrix[current_position[0]][current_position[1]] = "P"
        else:
            initial_string = initial_string[:-1]

print(initial_string)
print(*[''.join(r) for r in matrix], sep="\n")
