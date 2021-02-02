N = int(input())
first_diagonal = []
second_diagonal = []
matrix = [[int(el) for el in input().split(", ")]for r in range(N)]
for index in range(N):
    first_diagonal.append(matrix[index][index])
    second_diagonal.append(matrix[index][-1-index])
print(f"First diagonal: {', '.join(map(str,first_diagonal))}. Sum: {sum(first_diagonal)}")
print(f"Second diagonal: {', '.join(map(str,second_diagonal))}. Sum: {sum(second_diagonal)}")
