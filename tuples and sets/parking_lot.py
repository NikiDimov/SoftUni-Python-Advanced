n = int(input())
cars = set()
for _ in range(n):
    command = input().split(", ")
    direction, car_number = command[0], command[1]
    if direction == "IN":
        cars.add(car_number)
    elif direction == "OUT":
        cars.remove(car_number)
if len(cars) > 0:
    for car in cars:
        print(car)
else:
    print("Parking Lot is Empty")
    