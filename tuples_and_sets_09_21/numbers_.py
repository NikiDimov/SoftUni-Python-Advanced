first_line = set(input().split())
second_line = set(input().split())
N = int(input())
for _ in range(N):
    command = input().split()
    if command[0] == 'Add':
        if command[1] == 'First':
            sequence = command[2:]
            first_line = first_line.union(sequence)
        elif command[1] == 'Second':
            sequence = command[2:]
            second_line = second_line.union(sequence)
    elif command[0] == 'Remove':
        if command[1] == 'First':
            sequence = command[2:]
            first_line = first_line.difference(sequence)
        elif command[1] == 'Second':
            sequence = command[2:]
            second_line = second_line.difference(sequence)
    elif command[0] == 'Check':
        if first_line.issubset(second_line) or second_line.issubset(first_line):
            print(True)
        else:
            print(False)
first_line = {int(el) for el in first_line}
second_line = {int(el) for el in second_line}
print(', '.join(map(str, sorted(first_line))))
print(', '.join(map(str, sorted(second_line))))
