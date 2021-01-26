rows, cols = [int(el) for el in input().split()]
snake = input()
matrix = []
result = ""
counter = 0
while len(result) <= rows * cols:
    result += snake
result = result[:rows*cols]
while not len(result) == 0:
    matrix.append(result[:cols])
    result = result.replace(result[:cols], "", 1)
for el in matrix:
    counter += 1
    if counter % 2 == 1:
        print(el)
    else:
        print(el[::-1])

