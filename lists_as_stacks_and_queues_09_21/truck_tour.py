from collections import deque
N = int(input())
stations = deque()
for _ in range(N):
    stations.append(input())
for big_circle in range(N):
    is_valid = True
    tank_petrol = 0
    for small_circle in range(N):
        current_station = stations[small_circle]
        petrol, distance_to_the_next_station = current_station.split()
        petrol, distance_to_the_next_station = int(petrol), int(distance_to_the_next_station)
        tank_petrol += petrol - distance_to_the_next_station
        if tank_petrol < 0:
            is_valid = False
            stations.append(stations.popleft())
            break
    if is_valid:
        print(big_circle)
        break


