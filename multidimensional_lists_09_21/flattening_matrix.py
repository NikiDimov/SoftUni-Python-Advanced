rows = int(input())
flattening_matrix = [int(c) for r in range(rows) for c in input().split(', ')]
print(flattening_matrix)
