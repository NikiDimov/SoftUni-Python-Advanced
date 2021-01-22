N = int(input())
matrix = []
for row in range(N):
    matrix.append(list(input()))
symbol = input()
find_symbol = False
for row in range(N):
    if find_symbol is False:
        for col in range(N):
            if matrix[row][col] == symbol:
                find_symbol = True
                print(f"({row}, {col})")
                break
if find_symbol is False:
    print(f"{symbol} does not occur in the matrix")
