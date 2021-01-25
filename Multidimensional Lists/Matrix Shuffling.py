rows, cols = [int(el) for el in input().split()]
matrix = []
for _ in range(rows):
    matrix.append(input().split())
command = input()
while not command == "END":
    text = command.split()
    if text[0] == "swap" and len(text) == 5:
        row1, col1, row2, col2 = int(text[1]), int(text[2]), int(text[3]), int(text[4])
        if 0 <= row1 < rows and 0 <= row2 < rows and 0 <= col1 < cols and 0 <= col2 < cols:
            save_the_value = matrix[row1][col1]
            matrix[row1][col1] = matrix[row2][col2]
            matrix[row2][col2] = save_the_value
            for r in matrix:
                print(' '.join(r))
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")

    command = input()
