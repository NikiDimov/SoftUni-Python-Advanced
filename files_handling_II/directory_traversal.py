import os


def get_report_for_file_extensions(files):
    file_report = {}
    for el in files:
        value, key = el.split(".")
        if key not in file_report:
            file_report[key] = []
        file_report[key].append(value)
    return dict(sorted(file_report.items(), key=lambda x: x[0]))


def write_result_to_file(report):
    result = ""
    for key, value in report.items():
        result += f".{key}\n"
        for el in value:
            result += f"- - - {el}.{key}\n"

    with open("report.txt", "w") as file:
        file.write(''.join(result))


dir_content = os.listdir()
files = [el for el in dir_content if "." in el]
report = get_report_for_file_extensions(files)
write_result_to_file(report)

