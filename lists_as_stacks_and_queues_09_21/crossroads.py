from collections import deque

green_light = int(input())
free_window = int(input())
queue_of_cars = deque()
total_passed_cars = 0
command = input()
while not command == 'END':
    if command == "green":
        seconds_left = green_light
        while seconds_left > 0:
            if not queue_of_cars:
                break
            current_car = queue_of_cars.popleft()
            seconds_left -= len(current_car)
            if seconds_left < 0:
                car_index = seconds_left + len(current_car) + free_window
                if car_index >= len(current_car):
                    total_passed_cars += 1
                else:
                    print(f"A crash happened!\n{current_car} was hit at {current_car[car_index]}.")
                    exit()
            else:
                total_passed_cars += 1
    else:
        queue_of_cars.append(command)
    command = input()
print(f"Everyone is safe.")
print(f"{total_passed_cars} total cars passed the crossroads.")

