symbols = {"-", ",", ".", "!", "?"}
file = open('text.txt', 'r')
result = file.readlines()
n = len(result)
for i in range(0, n, 2):
    current_line = result[i].split()
    for k in range(len(current_line)):
        for el in current_line[k]:
            if el in symbols:
                current_line[k] = current_line[k].replace(el, '@')
    print(' '.join(current_line[::-1]))
file.close()
