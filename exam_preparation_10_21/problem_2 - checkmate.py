matrix = [input().split() for row in range(8)]
king = []
king_is_safe = True


def checker(x, y, *args):
    global king_is_safe
    if x not in range(0, 8) or y not in range(0, 8):
        return
    if matrix[x][y] == 'Q':
        king_is_safe = False
        print([x, y])
        return
    return checker(x+args[0], y+args[1], *args)


for r in range(8):
    for c in range(8):
        if matrix[r][c] == 'K':
            king = [r, c]
            break

r, c = king[0], king[1]
checker(r, c, -1, 0)
checker(r, c, 1, 0)
checker(r, c, 0, -1)
checker(r, c, 0, 1)
checker(r, c, -1, -1)
checker(r, c, -1, 1)
checker(r, c, 1, 1)
checker(r, c, 1, -1)

if king_is_safe:
    print("The king is safe!")
