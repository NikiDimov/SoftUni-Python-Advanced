# Ordinary solution:
# rows, cols = input().split()
# matrix = []
# counter = 0
# for r in range(97, 97 + int(rows)):
#     row = []
#     for c in range(97, 97 + int(cols)):
#         row.append(chr(r) + chr(c + counter) + chr(r))
#     matrix.append(row)
#     counter += 1
# for el in matrix:
#     print(" ".join(map(str, el)))

# Comprehension:
rows, cols = [int(el) for el in input().split()]
matrix = [[f"{chr(num)}{chr(nested_num)}{chr(num)}" for nested_num in range(num, num + cols)] for num in
          range(97, 97 + rows)]
print(*[" ".join(map(str, el)) for el in matrix], sep="\n")
