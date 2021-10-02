import re

words = 'words.txt'
input_file = 'input.txt'

file_1 = open(words, 'r')
text_1 = file_1.read().split()

file_2 = open(input_file, 'r')
text_2 = file_2.readlines()

result = {}
for word in text_1:
    for line in text_2:
        line = line.lower()
        pattern = fr'\b{word}\b'
        res = re.findall(pattern, line)
        if word not in result:
            result[word] = 0
        result[word] += len(res)

result = sorted(result.items(), key=lambda x: -x[1])
output = [f'{key}-{val}' for key, val in result]

with open('output.txt', 'w') as file:
    file.write('\n'.join(output))
