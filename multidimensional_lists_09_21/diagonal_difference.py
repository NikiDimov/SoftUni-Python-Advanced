N = int(input())
matrix = [[int(c) for c in input().split()] for r in range(N)]
primary_diagonal = [matrix[i][i] for i in range(N)]
secondary_diagonal = [matrix[i][-i - 1] for i in range(N)]
print(abs(sum(primary_diagonal)-sum(secondary_diagonal)))
