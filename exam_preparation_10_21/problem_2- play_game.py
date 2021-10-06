N = int(input())
matrix = [input().split() for row in range(N)]
path = []
current_position = []
TARGET = 100
coins = 0
commands = ['up', 'down', 'left', 'right']
mission_complete = True


def check_validation(x, y):
    global current_position
    global coins
    global mission_complete
    if x in range(0, N) and y in range(0, N):
        if not matrix[x][y] == 'X':
            coins += int(matrix[x][y])
            current_position = [x, y]
            path.append(current_position)
            return True
    coins = coins // 2
    print(f"Game over! You've collected {coins} coins.")
    mission_complete = False
    return False


for r in range(N):
    for c in range(N):
        if matrix[r][c] == 'P':
            current_position = [r, c]
            break

while True:
    if coins >= TARGET:
        break
    command = input()
    row, col = current_position[0], current_position[1]
    matrix[row][col] = '0'
    if command == 'left':
        if not check_validation(row, col - 1):
            break
    elif command == 'right':
        if not check_validation(row, col + 1):
            break
    elif command == 'up':
        if not check_validation(row - 1, col):
            break
    elif command == 'down':
        if not check_validation(row + 1, col):
            break

if mission_complete:
    print(f"You won! You've collected {coins} coins.")
print(f"Your path:")
print(*path, sep='\n')
