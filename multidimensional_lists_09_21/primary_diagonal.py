N = int(input())
matrix = [[int(c) for c in input().split()] for r in range(N)]
sum_primary_diagonal = 0
for i in range(N):
    sum_primary_diagonal += matrix[i][i]
print(sum_primary_diagonal)