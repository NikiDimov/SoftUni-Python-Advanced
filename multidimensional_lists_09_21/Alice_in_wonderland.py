N = int(input())
matrix = [[c for c in input().split()] for r in range(N)]
alice_pos = []
total_bags = 0
she_made_it = True


def interrupt_game(x, y):
    global total_bags
    global she_made_it
    global alice_pos
    alice_pos = [x, y]
    if x not in range(0, N) or y not in range(0, N):
        print("Alice didn't make it to the tea party.")
        she_made_it = False
        return True
    if matrix[x][y] == 'R':
        matrix[x][y] = '*'
        print("Alice didn't make it to the tea party.")
        she_made_it = False
        return True
    if matrix[x][y] == '.':
        matrix[x][y] = '*'
        return False
    if matrix[x][y].isdigit():
        total_bags += int(matrix[x][y])
        matrix[x][y] = '*'
        return False


for r in range(N):
    for c in range(N):
        if matrix[r][c] == "A":
            alice_pos = [r, c]
while total_bags < 10:
    command = input()
    r = alice_pos[0]
    c = alice_pos[1]
    matrix[r][c] = '*'
    if command == 'up':
        if interrupt_game(r-1, c):
            break
    elif command == 'down':
        if interrupt_game(r+1, c):
            break
    elif command == 'left':
        if interrupt_game(r, c-1):
            break
    elif command == 'right':
        if interrupt_game(r, c+1):
            break
if she_made_it:
    print("She did it! She went to the party.")
for row in matrix:
    print(*row)
