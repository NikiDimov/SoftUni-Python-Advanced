text = input()
parentheses = []

for i in range(len(text)):
    if text[i] == "(":
        parentheses.append(i)
    elif text[i] == ")":
        starting_pont = parentheses.pop()
        print(text[starting_pont:i+1])
