def get_magic_triangle(n):
    current_triangle = [[1], [1, 1]]
    for i in range(3, n + 1):
        row = [1]
        for y in range(len(current_triangle[-1]) - 1):
            row.append(current_triangle[-1][y] + current_triangle[-1][y + 1])
        row += [1]
        current_triangle.append(row)
    return current_triangle


print(get_magic_triangle(7))
