N = int(input())
matrix = [[c for c in input().split()] for r in range(N)]
bunny_pos = []
directions = ["up", "down", "left", "right"]
max_eggs = 0
eggs_pos = []
dir = ''


def eggs_generator():
    global current_eggs
    if r not in range(0, N) or c not in range(0, N):
        return False
    if matrix[r][c] == 'X':
        return False
    current_eggs += int(matrix[r][c])
    current_eggs_positions.append([r, c])
    return True


def checker():
    global max_eggs
    global eggs_pos
    global dir
    if current_eggs >= max_eggs:
        max_eggs = current_eggs
        eggs_pos = current_eggs_positions
        dir = direction


for r in range(N):
    for c in range(N):
        if matrix[r][c] == 'B':
            bunny_pos = [r, c]
for direction in directions:
    current_eggs = 0
    current_eggs_positions = []
    r = bunny_pos[0]
    c = bunny_pos[1]
    if direction == "up":
        while True:
            r -= 1
            if eggs_generator():
                checker()
            else:
                break
    elif direction == "down":
        while True:
            r += 1
            if eggs_generator():
                checker()
            else:
                break
    elif direction == "left":
        while True:
            c -= 1
            if eggs_generator():
                checker()
            else:
                break
    elif direction == "right":
        while True:
            c += 1
            if eggs_generator():
                checker()
            else:
                break
print(dir)
for row in eggs_pos:
    print(row)
print(max_eggs)

