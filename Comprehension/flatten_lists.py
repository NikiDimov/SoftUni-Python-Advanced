
print(*[" ".join(el.split()) for el in input().split("|")[::-1] if not (el == " " or el == "")])
