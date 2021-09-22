rows, columns = [int(el) for el in input().split()]
snake = input()
length = rows * columns
long_snake = ''
counter = 0
while len(long_snake) < length:
    long_snake += snake
long_snake = long_snake[:length]
while long_snake:
    counter += 1
    if counter % 2 == 0:
        print(long_snake[:columns][::-1])
    else:
        print(long_snake[:columns])
    long_snake = long_snake[columns:]


