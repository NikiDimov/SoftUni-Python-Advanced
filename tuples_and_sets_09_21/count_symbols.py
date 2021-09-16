line = tuple(input())
result = {}
for el in line:
    if el not in result:
        result[el] = 0
    result[el] = line.count(el)
for key, value in sorted(result.items()):
    print(f"{key}: {value} time/s")
