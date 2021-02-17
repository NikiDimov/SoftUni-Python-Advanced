import os


def create_file(file_name):
    with open(file_name, "w") as file:
        file.write("")


def add_content(file_name, content):
    with open(file_name, "a") as file:
        file.write(content + "\n")


def replace_content(file_name, content_to_replace, new_content):
    try:
        with open(file_name, "r") as file:
            list1 = file.readlines()
            new_list = [s.replace(content_to_replace, new_content) if content_to_replace in s else s for s in list1]
        with open(file_name, "w") as file:
            file.write("".join(new_list))
    except FileNotFoundError:
        print("Error occurred")


def delete_file(file_name):
    try:
        os.remove(file_name)
    except FileNotFoundError:
        print("Error occurred")


command = input()
while not command == "End":
    text = command.split("-")
    if text[0] == "Create":
        create_file(text[1])
    elif text[0] == "Add":
        add_content(text[1], text[2])
    elif text[0] == "Replace":
        replace_content(text[1], text[2], text[3])
    elif text[0] == "Delete":
        delete_file(text[1])
    command = input()
