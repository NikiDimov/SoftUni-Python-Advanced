matrix = [[int(el) for el in input().split()] for _ in range(int(input()))]
command = input()
while not command == "END":
    action, row, col, value = command.split()
    row, col, value = int(row), int(col), int(value)
    if not (0 <= row < len(matrix) and 0 <= col < len(matrix[0])):
        print(f"Invalid coordinates")
    elif action == "Add":
        matrix[row][col] += value
    elif action == "Subtract":
        matrix[row][col] -= value
    command = input()
print(*[' '.join(map(str, r)) for r in matrix], sep="\n")
