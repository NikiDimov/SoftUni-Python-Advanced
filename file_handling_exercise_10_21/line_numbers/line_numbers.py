punctuation_marks = (range(33, 48), range(58, 64), range(91, 97), range(123, 127))


def count_punctuation(text):
    counter = 0
    for el in text:
        for mark_range in punctuation_marks:
            if ord(el) in mark_range:
                counter += 1
                break
    return counter


def count_characters(text):
    counter = 0
    for el in text.split():
        counter += len(el)
    return counter


file = open('text.txt', 'r')
output = 'output.txt'
with open(output, 'w') as file_2:
    count = 0
    result = []
    while True:
        text = file.readline()
        if text == '':
            break
        if text[-1] == '\n':
            text = text[:-1]
        count += 1
        chars = count_characters(text)
        punctuations = count_punctuation(text)
        result.append(f"Line {count}: {text} ({chars - punctuations})({punctuations})")
    file_2.write('\n'.join(result))
