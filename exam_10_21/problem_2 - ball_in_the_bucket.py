matrix = [input().split() for row in range(6)]
total_points = 0


def checker(x, y):
    if x not in range(0, 6) or y not in range(0, 6):
        return False
    if not matrix[x][y] == 'B':
        return False
    return True


def get_prize(points):
    prize = ''
    if 100 <= points <= 199:
        prize = "Football"
    elif 200 <= points <= 299:
        prize = "Teddy Bear"
    elif points >= 300:
        prize = "Lego Construction Set"
    return prize


def get_points(x, y, step):
    global total_points
    if x not in range(0, 6):
        return
    if matrix[x][y].isdigit():
        total_points += int(matrix[x][y])
    get_points(x + step, y, step)


for _ in range(3):
    shot = eval(input())
    r, c = shot[0], shot[1]
    if checker(r, c):
        get_points(r, c, -1)
        get_points(r, c, 1)
        matrix[r][c] = '0'

prize = get_prize(total_points)
if prize:
    print(f"Good job! You scored {total_points} points, and you've won {prize}.")
else:
    print(f"Sorry! You need {100 - total_points} points more to win a prize.")
