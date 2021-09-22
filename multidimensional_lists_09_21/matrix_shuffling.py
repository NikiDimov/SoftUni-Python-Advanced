rows, columns = [int(el) for el in input().split()]
matrix = [[c for c in input().split()] for r in range(rows)]
command = input()
while not command == "END":
    data = command.split()
    if len(data) != 5:
        print("Invalid input!")
        command = input()
        continue
    row1, col1, row2, col2 = int(data[1]), int(data[2]), int(data[3]), int(data[4])
    if not data[0] == 'swap' or row1 not in range(0, rows) \
            or row2 not in range(0, rows) or col1 not in range(0, columns) or col2 not in range(0, columns):
        print("Invalid input!")
    else:
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        for row in matrix:
            print(*row)
    command = input()
