from collections import deque

water = int(input())
name = input()
queue_of_people = deque()
while not name == 'Start':
    queue_of_people.append(name)
    name = input()
command = input()
while not command == 'End':
    data = command.split()
    if not data[0] == 'refill':
        litters = int(data[0])
        current_person = queue_of_people.popleft()
        if litters <= water:
            print(f"{current_person} got water")
            water -= litters
        else:
            print(f"{current_person} must wait")
    else:
        litters = int(data[1])
        water += litters
    command = input()
print(f"{water} liters left")
