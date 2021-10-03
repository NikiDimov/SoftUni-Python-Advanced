import os

command = input()
while not command == 'End':
    data = command.split("-")
    action = data[0]
    file_name = data[1]
    if action == "Create":
        with open(file_name, 'w') as file:
            pass
    elif action == "Add":
        content = data[2]
        with open(file_name, 'a') as file:
            file.write(content + '\n')
    elif action == "Replace":
        old_string, new_string = data[2], data[3]
        try:
            with open(file_name, 'r') as file:
                content = file.read()
            with open(file_name, 'w') as file:
                content = content.replace(old_string, new_string)
                file.write(content)
        except FileNotFoundError:
            print("An error occurred")
    elif action == "Delete":
        try:
            os.remove(file_name)
        except FileNotFoundError:
            print("An error occurred")
    command = input()
