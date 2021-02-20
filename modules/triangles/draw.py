def draw_line(n):
    for k in range(1, n + 1):
        print(k, end=" ")
    print()


def draw_triangle(num):
    for i in range(1, num + 1):
        draw_line(i)
    for i in range(num - 1, 0, -1):
        draw_line(i)

