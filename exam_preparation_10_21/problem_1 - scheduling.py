from collections import deque

jobs = deque(int(el) for el in input().split(', '))
target_index = int(input())
indices = deque(i for i in range(len(jobs)))
cycles = 0


def rotate():
    jobs.append(jobs.popleft())
    indices.append(indices.popleft())


def checker():
    if jobs.count(jobs[0]) > 1:
        while not indices[0] == min(indices):
            rotate()


while True:
    if not jobs[0] == min(jobs):
        rotate()
    else:
        checker()
        cycles += jobs.popleft()
        if indices.popleft() == target_index:
            break
print(cycles)
