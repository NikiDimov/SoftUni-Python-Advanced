text = input()
stack = []

for index in range(len(text)):
    el = text[index]
    if el == "(":
        stack.append(index)
    elif el == ")":
        j = stack.pop()
        print(text[j:index+1])

