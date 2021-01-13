from collections import deque
quantity = int(input())
names_queue = deque()
command = input()
while not command == "Start":
    names_queue.append(command)
    command = input()
command = input()
while not command == "End":
    if command.isdigit():
        command = int(command)
        if command <= quantity:
            print(f"{names_queue.popleft()} got water")
            quantity -= command
        else:
            print(f"{names_queue.popleft()} must wait")
    elif command.split()[0] == "refill":
        liters = int(command.split()[1])
        quantity += liters
    command = input()
print(f"{quantity} liters left")
