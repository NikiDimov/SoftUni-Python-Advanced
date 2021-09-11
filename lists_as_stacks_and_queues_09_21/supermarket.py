from collections import deque

name = input()
queue_line = deque([])
while not name == 'End':
    if name == "Paid":
        while queue_line:
            print(queue_line.popleft())
        name = input()
        continue
    queue_line.append(name)
    name = input()
print(f"{len(queue_line)} people remaining.")
