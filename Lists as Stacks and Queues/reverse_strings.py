text = input()
stack = []
new_text = ""
for el in text:
    stack.append(el)
while stack:
    new_text += stack.pop()
print(new_text)


