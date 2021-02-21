from collections import deque
line = [int(el)for el in input().split(", ")]
line = deque(line)
index_of_job = int(input())
target = [line[index_of_job], index_of_job]
current_position = []
work_line = deque(sorted(line))
counter = 0
cycles = 0
while True:
    a = line.popleft()
    line.append(a)
    if a == work_line[0]:
        work_line.popleft()
        current_position = [a, counter]
        cycles += a
    if current_position == target:
        print(cycles)
        break
    if counter == len(line)-1:
        counter = 0
    else:
        counter += 1
