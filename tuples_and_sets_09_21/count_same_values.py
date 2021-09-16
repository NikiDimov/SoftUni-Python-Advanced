line = tuple(f'{float(el):.1f}'for el in input().split())
dict_line = {}
for el in line:
    if el not in dict_line:
        dict_line[el] = 0
    dict_line[el] = line.count(el)
for key, value in dict_line.items():
    print(f"{key} - {value} times")
