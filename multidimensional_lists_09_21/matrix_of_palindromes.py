row, column = [int(el) for el in input().split()]
matrix = [[f'{chr(97 + r) + chr(97 + r+c) + chr(97 + r)}' for c in range(column)] for r in range(row)]
for row in matrix:
    print(*row)
