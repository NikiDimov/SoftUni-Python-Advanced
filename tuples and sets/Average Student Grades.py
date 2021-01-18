n = int(input())
counter = 0
grades_list = []
students = {}
while counter < n:
    command = input().split()
    student = command[0]
    grade = float(command[1])
    if student not in students:
        students[student] = [grade]
    else:
        students[student].append(grade)
    counter += 1
for student, grades in students.items():
    print(f"{student} -> {' '.join(map(lambda x: f'{x:.2f}',grades))} (avg: {sum(grades)/len(grades):.2f})")

