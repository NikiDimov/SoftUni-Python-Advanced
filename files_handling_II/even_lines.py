def read_file(text):
    with open(text, "r") as file:
        list1 = file.readlines()
        return [list1[i] for i in range(len(list1)) if i % 2 == 0]


check_for = ("-", ".", ",", "!", "?")
our_text = read_file("text.txt")
result = []
for el in our_text:
    for s in check_for:
        if s in el:
            el = el.replace(s, "@")
    result.append(el)
print(*[' '.join(el.split()[::-1])for el in result], sep="\n")

