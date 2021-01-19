from collections import deque
names_queue = deque()
while True:
    command = input()
    if command == "End":
        print(f"{len(names_queue)} people remaining.")
        break
    elif command == "Paid":
        while names_queue:
            print(names_queue.popleft())
    else:
        names_queue.append(command)
