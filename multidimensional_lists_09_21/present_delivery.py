presents = int(input())
N = int(input())
matrix = [list(input().split()) for r in range(N)]
santa_pos = []
total_good_kids = 0
mission_complete = False
current_good_kids = 0


def cookie(x, y):
    global current_good_kids
    global presents
    global mission_complete
    if matrix[x][y] == 'V':
        current_good_kids += 1
        presents -= 1
        if current_good_kids == total_good_kids:
            mission_complete = True
    elif matrix[x][y] == 'X':
        presents -= 1
    matrix[x][y] = '-'


def santa_move(x, y):
    global santa_pos
    global presents
    global current_good_kids
    global mission_complete
    if x in range(0, N) and y in range(0, N):
        matrix[santa_pos[0]][santa_pos[1]] = '-'
        santa_pos = [x, y]
        if matrix[x][y] == 'V':
            presents -= 1
            current_good_kids += 1
            matrix[x][y] = 'S'
            if current_good_kids == total_good_kids:
                mission_complete = True
                return
            if presents == 0 and current_good_kids < total_good_kids:
                print("Santa ran out of presents!")
                return
        elif matrix[x][y] == 'X' or matrix[x][y] == '-':
            matrix[x][y] = 'S'
        elif matrix[x][y] == 'C':
            matrix[x][y] = 'S'
            cookie(x - 1, y)
            cookie(x, y + 1)
            cookie(x + 1, y)
            cookie(x, y - 1)
            if presents <= 0 and current_good_kids < total_good_kids:
                print("Santa ran out of presents!")


for r in range(N):
    for c in range(N):
        if matrix[r][c] == 'S':
            santa_pos = [r, c]
        if matrix[r][c] == 'V':
            total_good_kids += 1

command = input()
while presents > 0 and not command == 'Christmas morning':
    r = santa_pos[0]
    c = santa_pos[1]
    if command == 'up':
        santa_move(r - 1, c)
    elif command == 'down':
        santa_move(r + 1, c)
    elif command == 'left':
        santa_move(r, c - 1)
    elif command == 'right':
        santa_move(r, c + 1)
    if presents <= 0:
        break
    command = input()
for row in matrix:
    print(*row)
if mission_complete:
    print(f"Good job, Santa! {total_good_kids} happy nice kid/s.")
else:
    print(f"No presents for {total_good_kids - current_good_kids} nice kid/s.")
