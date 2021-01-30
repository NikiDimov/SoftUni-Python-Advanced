filters = [index for index in range(int(input()), int(input()) + 1) if any(index % i == 0 for i in range(2, 11))]
print(filters)
