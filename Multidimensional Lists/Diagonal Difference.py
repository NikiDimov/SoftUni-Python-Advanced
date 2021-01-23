N = int(input())
matrix = []
prime_sum = 0
secondary_sum = 0
for row in range(N):
    matrix.append(list(map(int, input().split())))
for i in range(N):
    prime_sum += matrix[i][i]
    secondary_sum += matrix[i][-1-i]
print(abs(prime_sum-secondary_sum))







