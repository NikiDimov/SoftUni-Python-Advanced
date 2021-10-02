file = open('numbers.txt', 'r')
total = 0
for num in file:
    total += int(num)
print(total)


