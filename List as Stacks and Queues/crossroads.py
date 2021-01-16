from collections import deque

lane = deque()
counter = 0
green_light = int(input())
free_window = int(input())
crash_happen = False
command = input()
while not command == "END":
    if not command == "green":
        lane.append(command)
    elif command == "green":
        if lane:
            current = lane.popleft()
            seconds_left = green_light - len(current)
            while seconds_left > 0:
                counter += 1
                if lane:
                    current = lane.popleft()
                    seconds_left -= len(current)
                else:
                    break
            if seconds_left == 0:
                counter += 1
            if free_window >= abs(seconds_left):
                if seconds_left < 0:
                    counter += 1
            else:
                idx = free_window + seconds_left
                print("A crash happened!")
                print(f"{current} was hit at {current[idx]}.")
                crash_happen = True
                break

    command = input()
if not crash_happen:
    print("Everyone is safe.")
    print(f"{counter} total cars passed the crossroads.")
