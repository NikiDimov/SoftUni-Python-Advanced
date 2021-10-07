name_1, name_2 = input().split(', ')
score_1 = 501
score_2 = 501
throw_1 = 0
throw_2 = 0
matrix = [input().split() for row in range(7)]
shots = 0


def turn(player, x, y, score, throw):
    if x not in range(0, 7) or y not in range(0, 7):
        return score
    if matrix[x][y].isdigit():
        score -= int(matrix[x][y])
    elif matrix[x][y] == 'D':
        current_sum = (int(matrix[x][0]) + int(matrix[0][y]) + int(matrix[x][6]) + int(matrix[6][y])) * 2
        score -= current_sum
    elif matrix[x][y] == 'T':
        current_sum = (int(matrix[x][0]) + int(matrix[0][y]) + int(matrix[x][6]) + int(matrix[6][y])) * 3
        score -= current_sum
    elif matrix[x][y] == 'B':
        print(f"{player} won the game with {throw} throws!")
        exit()
    return score


def checker(player, throw, score):
    if score <= 0:
        print(f"{player} won the game with {throw} throws!")
        exit()


while True:
    shots += 1
    r, c = eval(input())
    if shots % 2 == 1:
        throw_1 += 1
        score_1 = turn(name_1, r, c, score_1, throw_1)
        checker(name_1, throw_1, score_1)
    elif shots % 2 == 0:
        throw_2 += 1
        score_2 = turn(name_2, r, c, score_2, throw_2)
        checker(name_2, throw_2, score_2)
