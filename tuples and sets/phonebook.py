phone_book = {}
while True:
    command = input()
    if command.isdigit():
        break
    else:
        person, number = command.split("-")
        phone_book[person] = number
for _ in range(int(command)):
    name = input()
    if name not in phone_book:
        print(f"Contact {name} does not exist.")
    else:
        print(f"{name} -> {phone_book[name]}")
