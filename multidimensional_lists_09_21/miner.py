N = int(input())
commands = input().split()
matrix = [[c for c in input().split()] for r in range(N)]
current_position = []
total_coal = 0


def checker(x, y):
    global total_coal
    matrix[r][c] = '*'
    current_position[0] = x
    current_position[1] = y
    if matrix[x][y] == 'c':
        total_coal -= 1
        matrix[x][y] = 's'
        if total_coal == 0:
            print(f"You collected all coal! ({x}, {y})")
            exit()
    elif matrix[x][y] == 'e':
        print(f"Game over! ({x}, {y})")
        exit()


for r in range(N):
    for c in range(N):
        if matrix[r][c] == 's':
            current_position = [r, c]
        if matrix[r][c] == 'c':
            total_coal += 1
for command in commands:
    r = current_position[0]
    c = current_position[1]
    if command == "left":
        if c - 1 in range(0, N):
            checker(r, c - 1)
    elif command == "right":
        if c + 1 in range(0, N):
            checker(r, c + 1)
    elif command == "up":
        if r - 1 in range(0, N):
            checker(r - 1, c)
    elif command == "down":
        if r + 1 in range(0, N):
            checker(r + 1, c)

print(f"{total_coal} pieces of coal left. ({current_position[0]}, {current_position[1]})")
