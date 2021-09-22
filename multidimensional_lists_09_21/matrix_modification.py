N = int(input())
matrix = [[int(c) for c in input().split()] for r in range(N)]
command = input()
while not command == "END":
    data = command.split()
    act, row, col, val = data[0], int(data[1]), int(data[2]), int(data[3])
    if row not in range(0, N) or col not in range(0, N):
        print("Invalid coordinates")
        command = input()
        continue
    if act == "Add":
        matrix[row][col] += val
    elif act == "Subtract":
        matrix[row][col] -= val
    command = input()
for row in matrix:
    print(*row)
