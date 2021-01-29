size = int(input())
command = input().split()
field = []
row_index = 0
col_index = 0
counter_c = 0
game_over = False
current_position = [row_index, col_index]
for _ in range(size):
    field.append(input().split())

for r in range(size):
    if "s" in field[r]:
        row_index = r
        col_index = field[r].index("s")
        current_position = [row_index, col_index]
        field[row_index][col_index] = "*"
    if "c" in field[r]:
        counter_c += field[r].count("c")

for direction in command:
    if direction == "up" and 0 <= current_position[0] - 1 < size:
        current_position[0] -= 1
        if field[current_position[0]][current_position[1]] == "c":
            counter_c -= 1
            field[current_position[0]][current_position[1]] = "*"
            if counter_c == 0:
                print(f"You collected all coals! ({current_position[0]}, {current_position[1]})")
                break
        elif field[current_position[0]][current_position[1]] == "e":
            game_over = True
            print(f"Game over! ({current_position[0]}, {current_position[1]})")
            break
    elif direction == "right" and 0 <= current_position[1] + 1 < size:
        current_position[1] += 1
        if field[current_position[0]][current_position[1]] == "c":
            counter_c -= 1
            field[current_position[0]][current_position[1]] = "*"
            if counter_c == 0:
                print(f"You collected all coals! ({current_position[0]}, {current_position[1]})")
                break
        elif field[current_position[0]][current_position[1]] == "e":
            game_over = True
            print(f"Game over! ({current_position[0]}, {current_position[1]})")
            break
    elif direction == "left" and 0 <= current_position[1] - 1 < size:
        current_position[1] -= 1
        if field[current_position[0]][current_position[1]] == "c":
            counter_c -= 1
            field[current_position[0]][current_position[1]] = "*"
            if counter_c == 0:
                print(f"You collected all coals! ({current_position[0]}, {current_position[1]})")
                break
        elif field[current_position[0]][current_position[1]] == "e":
            game_over = True
            print(f"Game over! ({current_position[0]}, {current_position[1]})")
            break
    elif direction == "down" and 0 <= current_position[0] + 1 < size:
        current_position[0] += 1
        if field[current_position[0]][current_position[1]] == "c":
            counter_c -= 1
            field[current_position[0]][current_position[1]] = "*"
            if counter_c == 0:
                print(f"You collected all coals! ({current_position[0]}, {current_position[1]})")
                break
        elif field[current_position[0]][current_position[1]] == "e":
            print(f"Game over! ({current_position[0]}, {current_position[1]})")
            game_over = True
            break
if counter_c > 0 and game_over is False:
    print(f"{counter_c} coals left. ({current_position[0]}, {current_position[1]})")

