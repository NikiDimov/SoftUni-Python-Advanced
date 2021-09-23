matrix = [[c for c in input().split()] for r in range(5)]
position = []
target_position = []
total_shots = 0
targets_to_shoot = 0


def move(x, y):
    global position
    if x not in range(0, 5) or y not in range(0, 5):
        return
    if matrix[x][y] == 'x':
        return
    if matrix[x][y] == '.':
        matrix[position[0]][position[1]] = '.'
        position = [x, y]


def shoot(x, y):
    global total_shots
    if matrix[x][y] == 'x':
        total_shots += 1
        target_position.append([x, y])
        matrix[x][y] = '.'
        return True
    return False


for r in range(5):
    for c in range(5):
        if matrix[r][c] == 'A':
            position = [r, c]
        if matrix[r][c] == 'x':
            targets_to_shoot += 1

n = int(input())
for _ in range(n):
    command = input().split()
    r = position[0]
    c = position[1]
    if command[0] == "move":
        steps = int(command[2])
        direction = command[1]
        if direction == "right":
            move(r, c + steps)
        elif direction == "left":
            move(r, c - steps)
        elif direction == "up":
            move(r - steps, c)
        elif direction == "down":
            move(r + steps, c)
    elif command[0] == "shoot":
        direction = command[1]
        if direction == "right":
            while c + 1 in range(0, 5):
                c += 1
                if shoot(r, c):
                    break
        elif direction == "left":
            while c - 1 in range(0, 5):
                c -= 1
                if shoot(r, c):
                    break
        elif direction == "up":
            while r - 1 in range(0, 5):
                r -= 1
                if shoot(r, c):
                    break
        elif direction == "down":
            while r + 1 in range(0, 5):
                r += 1
                if shoot(r, c):
                    break
        if total_shots == targets_to_shoot:
            break
if total_shots == targets_to_shoot:
    print(f"Training completed! All {targets_to_shoot} targets hit.")
else:
    print(f"Training not completed! {targets_to_shoot-total_shots} targets left.")

for target in target_position:
    print(target)
