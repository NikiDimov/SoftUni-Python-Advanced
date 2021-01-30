from copy import deepcopy

N, M = [int(el) for el in input().split()]
layer = []
for index in range(N):
    layer.append(list(input()))
commands = list(input())
player_position = ()


def result_matrix(matrix):
    for row in matrix:
        print("".join(row))


def bunny_spread(matrix, rows, cols):
    update_matrix = deepcopy(matrix)
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == "B":
                if 0 <= col - 1 < cols and matrix[row][col - 1] != "B":
                    update_matrix[row][col - 1] = "B"
                if 0 <= col + 1 < cols and matrix[row][col + 1] != "B":
                    update_matrix[row][col + 1] = "B"
                if 0 <= row - 1 < rows and matrix[row - 1][col] != "B":
                    update_matrix[row - 1][col] = "B"
                if 0 <= row + 1 < rows and matrix[row + 1][col] != "B":
                    update_matrix[row + 1][col] = "B"
    return update_matrix


for r in range(N):
    if "P" in layer[r]:
        player_position = (r, layer[r].index("P"))

for command in commands:
    if command == "U":
        if 0 <= player_position[0] - 1 < N and layer[player_position[0] - 1][player_position[1]] != "B":
            layer[player_position[0]][player_position[1]] = "."
            layer[player_position[0] - 1][player_position[1]] = "P"
            player_position = (player_position[0] - 1, player_position[1])
            layer = bunny_spread(layer, N, M)
        elif 0 <= player_position[0] - 1 < N and layer[player_position[0] - 1][player_position[1]] == "B":
            player_position = (player_position[0] - 1, player_position[1])
            layer = bunny_spread(layer, N, M)
            result_matrix(layer)
            print(f"dead: {player_position[0]} {player_position[1]}")
            break
        else:
            layer = bunny_spread(layer, N, M)
            layer[player_position[0]][player_position[1]] = "."
            result_matrix(layer)
            print(f"won: {player_position[0]} {player_position[1]}")
            break
    elif command == "L":
        if 0 <= player_position[1] - 1 < N and layer[player_position[0]][player_position[1] - 1] != "B":
            layer[player_position[0]][player_position[1]] = "."
            layer[player_position[0]][player_position[1] - 1] = "P"
            player_position = (player_position[0], player_position[1] - 1)
            layer = bunny_spread(layer, N, M)
        elif 0 <= player_position[1] - 1 < N and layer[player_position[0]][player_position[1] - 1] == "B":
            player_position = (player_position[0], player_position[1] - 1)
            layer = bunny_spread(layer, N, M)
            result_matrix(layer)
            print(f"dead: {player_position[0]} {player_position[1]}")
            break
        else:
            layer = bunny_spread(layer, N, M)
            layer[player_position[0]][player_position[1]] = "."
            result_matrix(layer)
            print(f"won: {player_position[0]} {player_position[1]}")
            break
    elif command == "R":
        if 0 <= player_position[1] + 1 < N and layer[player_position[0]][player_position[1] + 1] != "B":
            layer[player_position[0]][player_position[1]] = "."
            layer[player_position[0]][player_position[1] + 1] = "P"
            player_position = (player_position[0], player_position[1] + 1)
            layer = bunny_spread(layer, N, M)
        elif 0 <= player_position[1] + 1 < N and layer[player_position[0]][player_position[1] + 1] == "B":
            player_position = (player_position[0], player_position[1] + 1)
            layer = bunny_spread(layer, N, M)
            result_matrix(layer)
            print(f"dead: {player_position[0]} {player_position[1]}")
            break
        else:
            layer = bunny_spread(layer, N, M)
            layer[player_position[0]][player_position[1]] = "."
            result_matrix(layer)
            print(f"won: {player_position[0]} {player_position[1]}")
            break

    elif command == "D":
        if 0 <= player_position[0] + 1 < N and layer[player_position[0] + 1][player_position[1]] != "B":
            layer[player_position[0]][player_position[1]] = "."
            layer[player_position[0] + 1][player_position[1]] = "P"
            player_position = (player_position[0] + 1, player_position[1])
            layer = bunny_spread(layer, N, M)
        elif 0 <= player_position[0] - 1 < N and layer[player_position[0] + 1][player_position[1]] == "B":

            player_position = (player_position[0] + 1, player_position[1])
            layer = bunny_spread(layer, N, M)
            result_matrix(layer)
            print(f"dead: {player_position[0]} {player_position[1]}")
            break
        else:
            layer = bunny_spread(layer, N, M)
            layer[player_position[0]][player_position[1]] = "."
            result_matrix(layer)
            print(f"won: {player_position[0]} {player_position[1]}")
            break

