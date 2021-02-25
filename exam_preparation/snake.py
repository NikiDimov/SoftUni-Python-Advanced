def move_snake(m, s_p, b, f_q):
    if m[s_p[0]][s_p[1]] == "*":
        f_q[0] += 1
        m[s_p[0]][s_p[1]] = "S"
    elif m[s_p[0]][s_p[1]] == "B":
        m[s_p[0]][s_p[1]] = "."
        if s_p[0] == b["first_burrow"][0]:
            s_p[0] = b["second_burrow"][0]
            s_p[1] = b["second_burrow"][1]
        elif s_p[0] == b["second_burrow"][0]:
            s_p[0] = b["first_burrow"][0]
            s_p[1] = b["first_burrow"][1]
        m[s_p[0]][s_p[1]] = "S"
    elif m[s_p[0]][s_p[1]] == "-":
        m[s_p[0]][s_p[1]] = "S"


N = int(input())
matrix = [list(input()) for r in range(N)]
snake_position = []
burrows = {}
food_quantity = [0]
for r in range(N):
    for c in range(N):
        if matrix[r][c] == "S":
            snake_position = [r, c]
        elif matrix[r][c] == "B":
            if "first_burrow" not in burrows:
                burrows["first_burrow"] = [r, c]
            burrows["second_burrow"] = [r, c]
while True:
    command = input()
    if command == "left" and 0 <= snake_position[1] - 1 < N:
        matrix[snake_position[0]][snake_position[1]] = "."
        snake_position[1] -= 1
        move_snake(matrix, snake_position, burrows, food_quantity)
    elif command == "right" and 0 <= snake_position[1] + 1 < N:
        matrix[snake_position[0]][snake_position[1]] = "."
        snake_position[1] += 1
        move_snake(matrix, snake_position, burrows, food_quantity)
    elif command == "up" and 0 <= snake_position[0] - 1 < N:
        matrix[snake_position[0]][snake_position[1]] = "."
        snake_position[0] -= 1
        move_snake(matrix, snake_position, burrows, food_quantity)
    elif command == "down" and 0 <= snake_position[0] + 1 < N:
        matrix[snake_position[0]][snake_position[1]] = "."
        snake_position[0] += 1
        move_snake(matrix, snake_position, burrows, food_quantity)
    else:
        print("Game over!")
        matrix[snake_position[0]][snake_position[1]] = "."
        break
    if food_quantity[0] == 10:
        print("You won! You fed the snake.")
        matrix[snake_position[0]][snake_position[1]] = "S"
        break
print(f"Food eaten: {food_quantity[0]}")
print(*[''.join(row) for row in matrix], sep="\n")
