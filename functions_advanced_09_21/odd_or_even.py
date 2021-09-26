def checker(command, line):
    result = 0
    if command == 'Odd':
        odds = [el for el in line if el % 2 == 1]
        result = sum(odds) * len(line)
    elif command == 'Even':
        evens = [el for el in line if el % 2 == 0]
        result = sum(evens) * len(line)
    return result


command = input()
line = [int(el) for el in input().split()]

print(checker(command, line))
