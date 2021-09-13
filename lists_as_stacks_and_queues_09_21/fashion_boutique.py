cloths = [int(el) for el in input().split()]
capacity_of_a_rack = int(input())
current_quantity = 0
total_racks = 1
while cloths:
    if current_quantity + cloths[-1] <= capacity_of_a_rack:
        current_quantity += cloths.pop()
    else:
        total_racks += 1
        current_quantity = 0

print(total_racks)