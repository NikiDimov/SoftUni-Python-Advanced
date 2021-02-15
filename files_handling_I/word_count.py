import re


def get_file_content(path_to_file):
    with open(path_to_file, "r") as file:
        text = "".join(file.readlines())
        return re.findall(r"[a-z']+", text.lower())


def create_file_result(res):
    with open("output.txt", "w") as file:
        file.writelines("\n".join(res))


path_to_words = "words.txt"
path_to_text = "input.txt"
result = {}
for el in get_file_content(path_to_words):
    if el in get_file_content(path_to_text):
        result[el] = get_file_content(path_to_text).count(el)

result = [f"{key}-{value}" for key, value in sorted(result.items(), key=lambda x: -x[1])]
create_file_result(result)
