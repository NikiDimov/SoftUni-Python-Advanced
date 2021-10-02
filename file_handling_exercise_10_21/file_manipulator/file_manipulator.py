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
            file_text = open(file_name, 'r')
            file_text = file_text.readlines()
            for i in range(len(file_text)):
                if old_string in file_text[i]:
                    file_text[i] = file_text[i].replace(old_string, new_string)
            with open(file_name, 'w') as file:
                file.write(''.join(file_text))
        except FileNotFoundError:
            print("An error occurred")
    elif action == "Delete":
        try:
            os.remove(file_name)
        except FileNotFoundError:
            print("An error occurred")
    command = input()
