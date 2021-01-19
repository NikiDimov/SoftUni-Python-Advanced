clothes = input().split()
clothes = [int(el) for el in clothes]
rack_capacity = int(input())
capacity = rack_capacity
total_racks = 1
while len(clothes) > 0:
    current_cloth = clothes.pop()
    rack_capacity -= current_cloth
    if rack_capacity < 0:
        clothes.append(current_cloth)
        rack_capacity = capacity
        total_racks += 1
print(total_racks)
