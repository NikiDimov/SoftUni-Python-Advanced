N = int(input())
parking_lot = set()
for _ in range(N):
    direction, car = input().split(", ")
    if direction == 'IN':
        if car not in parking_lot:
            parking_lot.add(car)
    elif direction == 'OUT':
        if car in parking_lot:
            parking_lot.remove(car)
if parking_lot:
    for car in parking_lot:
        print(car)
else:
    print("Parking Lot is Empty")