line = list(input())
dict_of_chars = {}
for el in line:
    dict_of_chars[el] = line.count(el)
dict_of_chars = dict(sorted(dict_of_chars.items(), key=lambda x: x[0]))
for key, value in dict_of_chars.items():
    print(f"{key}: {value} time/s")
    