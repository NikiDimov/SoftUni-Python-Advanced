def read_file(text):
    with open(text, "r") as file:
        return file.readlines()


def find_punctuations(our_text, check_for):
    dict_pu = {}
    for el in our_text:
        counter = 0
        for s in check_for:
            counter += el.count(s)
        dict_pu[el] = counter
    return dict_pu


def find_letters(our_text):
    dict_let = {}
    for el in our_text:
        counter = 0
        for l in el:
            if l.isalpha():
                counter += 1
        dict_let[el] = counter
    return dict_let


def final_result(text, puncts, letters):
    for i in range(len(text)):
        return "\n".join(
            [f"Line {i + 1}: {text[i][:-1]} ({letters[text[i]]})({puncts[text[i]]})" for i in range(len(text))])


our_text = read_file("text.txt")
check_for = ("-", ".", ",", "!", "?", "'")
dict_puncts = find_punctuations(our_text, check_for)
dict_letters = find_letters(our_text)
result = final_result(our_text, dict_puncts, dict_letters)
with open("output.txt", "w") as file2:
    file2.write(result)
