n = int(input())
matrix = [list(input()) for row in range(n)]
food_eaten = 0
snake_position = []
for r in range(n):
    for c in range(n):
        if matrix[r][c] == 'S':
            snake_position = [r, c]
            break


def out_of_range(x, y):
    global snake_position
    if x not in range(0, n) or y not in range(0, n):
        snake_position = [x, y]
        return True


def check_burrow(x, y):
    global snake_position
    if out_of_range(x, y):
        return
    if matrix[x][y] == 'B':
        matrix[x][y] = '.'
        for r in range(n):
            for c in range(n):
                if matrix[r][c] == 'B':
                    matrix[r][c] = 'S'
                    snake_position = [r, c]
                    return


def check_food(x, y):
    global food_eaten
    global snake_position
    if out_of_range(x, y):
        return
    if matrix[x][y] == '*':
        matrix[x][y] = 'S'
        food_eaten += 1
        snake_position = [x, y]


def step_on_empty(x, y):
    global snake_position
    if out_of_range(x, y):
        return
    if matrix[x][y] == '-':
        matrix[x][y] = 'S'
        snake_position = [x, y]


def move(x, y):
    check_burrow(x, y)
    check_food(x, y)
    step_on_empty(x, y)


row, col = snake_position[0], snake_position[1]
while row in range(0, n) and col in range(0, n) and food_eaten < 10:
    command = input()
    matrix[row][col] = '.'
    if command == 'up':
        move(row - 1, col)
    elif command == 'down':
        move(row + 1, col)
    elif command == 'left':
        move(row, col - 1)
    elif command == 'right':
        move(row, col + 1)
    row, col = snake_position[0], snake_position[1]

if food_eaten < 10:
    print("Game over!")
else:
    print("You won! You fed the snake.")
print(f"Food eaten: {food_eaten}")
for row in matrix:
    print(''.join(row))
