N = int(input())
matrix = [[c for c in list(input())] for r in range(N)]
symbol = input()
for r in range(N):
    for c in range(N):
        if matrix[r][c] == symbol:
            print((r, c))
            exit()
print(f"{symbol} does not occur in the matrix")
