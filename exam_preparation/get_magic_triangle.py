def get_magic_triangle(n):
    magic_triangle = [[1], [1, 1]]
    for r in range(2, n):
        current_row = []
        for c in range(len(magic_triangle[-1]) - 1):
            current_row.append(magic_triangle[-1][c] + magic_triangle[-1][c + 1])
        current_row.insert(0, 1)
        current_row.append(1)
        magic_triangle.append(current_row)
    return magic_triangle


print(get_magic_triangle(5))
