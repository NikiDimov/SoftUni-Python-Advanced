colors = input().split()
main_colors = ["red", "yellow", "blue"]
secondary_colors = {"orange": {'red', 'yellow'}, "purple": {'red', 'blue'}, "green": {'yellow', 'blue'}}
result_colors = []


def checker(first, last):
    result = ''
    if first + last in main_colors:
        result = first + last
    elif first + last in secondary_colors:
        result = first + last
    elif last + first in main_colors:
        result = last + first
    elif last + first in secondary_colors:
        result = last + first
    return result


while len(colors) > 1:
    color = checker(colors[0], colors[-1])
    if color:
        result_colors.append(color)
        colors = colors[1:-1]
    else:
        colors[0] = colors[0][:-1]
        colors[-1] = colors[-1][:-1]
        res = [colors[0], colors[-1]]
        colors = colors[1:-1]
        while '' in res:
            res.remove('')
        index = len(colors) // 2
        colors = colors[:index] + res + colors[index:]
if len(colors) == 1:
    while colors:
        if colors[0] in main_colors or colors[0] in secondary_colors:
            result_colors.append(colors[0])
            colors.pop()
        else:
            colors[0] = colors[0][:-1]
            if colors[0] == '':
                colors.pop()

final_output = []
for el in result_colors:
    if el in main_colors:
        final_output.append(el)
    elif el in secondary_colors:
        if secondary_colors[el].issubset(result_colors):
            final_output.append(el)
print(final_output)

