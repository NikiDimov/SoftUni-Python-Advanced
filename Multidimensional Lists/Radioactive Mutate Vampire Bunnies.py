# By Doncho 60/100
from collections import deque

BUNNY = 'B'
PLAYER = 'P'
EMPTY = '.'


def read_input(is_test=False):
    if is_test:
        lair = [
            ['.', '.', '.', '.', '.', '.', '.', 'B'],
            ['.', '.', '.', 'B', '.', '.', '.', '.'],
            ['.', '.', '.', '.', 'B', '.', '.', 'B'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', 'P', '.', '.', '.', '.', '.'],
        ]
        directions = 'ULLL'

        # lair = [
        #     ['.', '.', '.', '.', '.'],
        #     ['.', '.', '.', '.', '.'],
        #     ['.', 'B', '.', '.', '.'],
        #     ['.', '.', '.', 'P', '.'],
        # ]
        # directions = 'LLLLLLLL'

        return (lair, directions)

    rows_count, columns_count = [int(x) for x in input().split(' ')]
    lair = []
    for _ in range(rows_count):
        lair.append(list(input()))
    directions = input()

    return lair, directions


def in_range(value, max_value):
    return 0 <= value < max_value


def get_bunnies(lair):
    bunnies = []
    for row_index in range(len(lair)):
        for column_index in range(len(lair[0])):
            if lair[row_index][column_index] == BUNNY:
                bunnies.append((row_index, column_index))
    return bunnies


def get_player(lair):
    for row_index in range(len(lair)):
        if PLAYER in lair[row_index]:
            column_index = lair[row_index].index(PLAYER)
            return (row_index, column_index)


def get_next_move(position, dir):
    dir_deltas = {
        'U': (-1, 0),
        'D': (+1, 0),
        'L': (0, -1),
        'R': (0, +1),
    }
    (row_index, column_index) = position
    (row_delta, column_delta) = dir_deltas[dir]

    return row_index + row_delta, column_index + column_delta


def is_free_cell(lair, position):
    rows_count = len(lair)
    columns_count = len(lair[0])
    (row_index, column_index) = position

    return in_range(row_index, rows_count) \
           and in_range(column_index, columns_count) \
           and lair[row_index][column_index] != BUNNY


def spread_bunnies(lair, bunnies):
    for _ in range(len(bunnies)):
        bunny = bunnies.popleft()
        next_bunnies = [
            get_next_move(bunny, dir)
            for dir in 'UDLR'
        ]
        next_bunnies = [
            next_bunny
            for next_bunny in next_bunnies
            if is_free_cell(lair, next_bunny)
        ]

        for (row_index, col_index) in next_bunnies:
            lair[row_index][col_index] = BUNNY
            bunnies.append((row_index, col_index))


def is_win(lair, player):
    (row_index, column_index) = player
    return not in_range(row_index, len(lair)) \
           or not in_range(column_index, len(lair[0]))


def is_loss(lair, player):
    (row_index, column_index) = player
    return lair[row_index][column_index] == BUNNY


def print_result(lair, player, is_win):
    row_index, column_index = player
    [print(''.join(row)) for row in lair]
    if is_win:
        print(f'won: {row_index} {column_index}')
    else:
        print(f'dead: {row_index} {column_index}')


def play_game(lair, bunnies, player, directions):
    bunnies = deque(bunnies)
    row_index, column_index = player
    for dir in directions:
        spread_bunnies(lair, bunnies)
        next_row_index, next_column_index = get_next_move((row_index, column_index), dir)
        if is_win(lair, (next_row_index, next_column_index)):
            lair[row_index][column_index] = EMPTY
            print_result(lair, (row_index, column_index), is_win=True)
            break
        elif is_loss(lair, (next_row_index, next_column_index)):
            print_result(lair, (next_row_index, next_column_index), is_win=False)
            break
        lair[row_index][column_index] = EMPTY
        lair[next_row_index][next_column_index] = PLAYER
        row_index, column_index = next_row_index, next_column_index


lair, directions = read_input(is_test=False)
bunnies = get_bunnies(lair)
player = get_player(lair)

play_game(lair, bunnies, player, directions)

# -----------------------------------------------------------------------------------
# My Code : 50/100

# from copy import deepcopy
#
# N, M = [int(el) for el in input().split()]
# layer = []
# for index in range(N):
#     layer.append(list(input()))
# commands = list(input())
# player_position = ()
#
#
# def result_matrix(matrix):
#     for row in matrix:
#         print("".join(row))
#
#
# def bunny_spread(matrix, rows, cols):
#     update_matrix = deepcopy(matrix)
#     for row in range(rows):
#         for col in range(cols):
#             if matrix[row][col] == "B":
#                 if 0 <= col - 1 < cols and matrix[row][col - 1] != "B":
#                     update_matrix[row][col - 1] = "B"
#                 if 0 <= col + 1 < cols and matrix[row][col + 1] != "B":
#                     update_matrix[row][col + 1] = "B"
#                 if 0 <= row - 1 < rows and matrix[row - 1][col] != "B":
#                     update_matrix[row - 1][col] = "B"
#                 if 0 <= row + 1 < rows and matrix[row + 1][col] != "B":
#                     update_matrix[row + 1][col] = "B"
#     return update_matrix
#
#
# for r in range(N):
#     if "P" in layer[r]:
#         player_position = (r, layer[r].index("P"))
#
# for command in commands:
#     if command == "U":
#         if 0 <= player_position[0] - 1 < N and layer[player_position[0] - 1][player_position[1]] != "B":
#             layer[player_position[0]][player_position[1]] = "."
#             layer[player_position[0] - 1][player_position[1]] = "P"
#             player_position = (player_position[0] - 1, player_position[1])
#             layer = bunny_spread(layer, N, M)
#         elif 0 <= player_position[0] - 1 < N and layer[player_position[0] - 1][player_position[1]] == "B":
#             player_position = (player_position[0] - 1, player_position[1])
#             layer = bunny_spread(layer, N, M)
#             result_matrix(layer)
#             print(f"dead: {player_position[0]} {player_position[1]}")
#             break
#         else:
#             layer = bunny_spread(layer, N, M)
#             layer[player_position[0]][player_position[1]] = "."
#             result_matrix(layer)
#             print(f"won: {player_position[0]} {player_position[1]}")
#             break
#     elif command == "L":
#         if 0 <= player_position[1] - 1 < N and layer[player_position[0]][player_position[1] - 1] != "B":
#             layer[player_position[0]][player_position[1]] = "."
#             layer[player_position[0]][player_position[1] - 1] = "P"
#             player_position = (player_position[0], player_position[1] - 1)
#             layer = bunny_spread(layer, N, M)
#         elif 0 <= player_position[1] - 1 < N and layer[player_position[0]][player_position[1] - 1] == "B":
#             player_position = (player_position[0], player_position[1] - 1)
#             layer = bunny_spread(layer, N, M)
#             result_matrix(layer)
#             print(f"dead: {player_position[0]} {player_position[1]}")
#             break
#         else:
#             layer = bunny_spread(layer, N, M)
#             layer[player_position[0]][player_position[1]] = "."
#             result_matrix(layer)
#             print(f"won: {player_position[0]} {player_position[1]}")
#             break
#     elif command == "R":
#         if 0 <= player_position[1] + 1 < N and layer[player_position[0]][player_position[1] + 1] != "B":
#             layer[player_position[0]][player_position[1]] = "."
#             layer[player_position[0]][player_position[1] + 1] = "P"
#             player_position = (player_position[0], player_position[1] + 1)
#             layer = bunny_spread(layer, N, M)
#         elif 0 <= player_position[1] + 1 < N and layer[player_position[0]][player_position[1] + 1] == "B":
#             player_position = (player_position[0], player_position[1] + 1)
#             layer = bunny_spread(layer, N, M)
#             result_matrix(layer)
#             print(f"dead: {player_position[0]} {player_position[1]}")
#             break
#         else:
#             layer = bunny_spread(layer, N, M)
#             layer[player_position[0]][player_position[1]] = "."
#             result_matrix(layer)
#             print(f"won: {player_position[0]} {player_position[1]}")
#             break
#
#     elif command == "D":
#         if 0 <= player_position[0] + 1 < N and layer[player_position[0] + 1][player_position[1]] != "B":
#             layer[player_position[0]][player_position[1]] = "."
#             layer[player_position[0] + 1][player_position[1]] = "P"
#             player_position = (player_position[0] + 1, player_position[1])
#             layer = bunny_spread(layer, N, M)
#         elif 0 <= player_position[0] - 1 < N and layer[player_position[0] + 1][player_position[1]] == "B":
#
#             player_position = (player_position[0] + 1, player_position[1])
#             layer = bunny_spread(layer, N, M)
#             result_matrix(layer)
#             print(f"dead: {player_position[0]} {player_position[1]}")
#             break
#         else:
#             layer = bunny_spread(layer, N, M)
#             layer[player_position[0]][player_position[1]] = "."
#             result_matrix(layer)
#             print(f"won: {player_position[0]} {player_position[1]}")
#             break
