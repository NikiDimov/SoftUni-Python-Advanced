file = open('text.txt', 'r')
text = file.readlines()
for el in text:
    if text.index(el) == len(text)-1:
        print(el)
    else:
        print(el[:-1])


