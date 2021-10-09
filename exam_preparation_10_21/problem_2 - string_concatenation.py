text = input()
N = int(input())
matrix = [list(input()) for r in range(N)]


def find_player():
    for r in range(N):
        for col in range(N):
            if matrix[r][col] == 'P':
                return r, col


def move(x, y, text_line):
    global player_position
    if x not in range(0, N) or y not in range(0, N):
        return text_line[:-1]
    if str(matrix[x][y]).isalpha():
        text_line += matrix[x][y]
    matrix[player_position[0]][player_position[1]] = '-'
    matrix[x][y] = 'P'
    player_position = x, y
    return text_line


player_position = find_player()

M = int(input())
for _ in range(M):
    r, c = player_position[0], player_position[1]
    command = input()
    if command == 'left':
        text = move(r, c - 1, text)
    elif command == 'right':
        text = move(r, c + 1, text)
    elif command == 'up':
        text = move(r - 1, c, text)
    elif command == 'down':
        text = move(r + 1, c, text)
print(text)
for row in matrix:
    print(''.join(row))
