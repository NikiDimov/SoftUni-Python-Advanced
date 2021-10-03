import os


def traverse_directories(dir_path):
    for file in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, file)):
            extension = '.' + file.split('.')[-1]
            if extension not in report_dict:
                report_dict[extension] = []
            report_dict[extension].append(file)
        elif os.path.isdir(os.path.join(dir_path, file)):
            traverse_directories(os.path.join(dir_path, file))


directory = input()
report_dict = {}
traverse_directories(directory)

report_dict = dict(sorted(report_dict.items(), key=lambda x: (x[0], sorted(x[1]))))

path_desk = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') + os.path.sep + 'report.txt'
with open(path_desk, 'w') as desktop_file:
    for key, value in report_dict.items():
        desktop_file.write(key + '\n')
        for el in value:
            desktop_file.write(f'- - - {el}\n')

