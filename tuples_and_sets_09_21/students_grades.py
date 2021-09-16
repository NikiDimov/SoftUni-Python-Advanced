N = int(input())
dict_of_students = {}
for _ in range(N):
    student, grade = input().split()
    grade = float(grade)
    if student not in dict_of_students:
        dict_of_students[student] = []
    dict_of_students[student].append(grade)
for key, value in dict_of_students.items():
    print(f"{key} -> {' '.join([f'{el:.2f}'for el in value])} (avg: {sum(value)/len(value):.2f})")

