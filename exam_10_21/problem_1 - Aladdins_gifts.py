from collections import deque

materials = [int(el) for el in input().split()]
magic_levels = deque(int(el) for el in input().split())

total_gifts = {"Diamond Jewellery": 0, "Gemstone": 0, "Gold": 0, "Porcelain Sculpture": 0}


def checker(total):
    if 100 <= total <= 199:
        total_gifts["Gemstone"] += 1
    elif 200 <= total <= 299:
        total_gifts["Porcelain Sculpture"] += 1
    elif 300 <= total <= 399:
        total_gifts["Gold"] += 1
    elif 400 <= total <= 499:
        total_gifts["Diamond Jewellery"] += 1
    else:
        return False
    materials.pop()
    magic_levels.popleft()
    return True


while materials and magic_levels:
    current_sum = materials[-1] + magic_levels[0]
    if not checker(current_sum):
        if current_sum < 100:
            if current_sum % 2 == 0:
                current_sum = materials[-1] * 2 + magic_levels[0] * 3
                if not checker(current_sum):
                    materials.pop()
                    magic_levels.popleft()
            else:
                current_sum = materials[-1] * 2 + magic_levels[0] * 2
                if not checker(current_sum):
                    materials.pop()
                    magic_levels.popleft()
        elif current_sum > 499:
            current_sum = (materials[-1] + magic_levels[0]) / 2
            if not checker(current_sum):
                materials.pop()
                magic_levels.popleft()
        else:
            materials.pop()
            magic_levels.popleft()

if (total_gifts["Gemstone"] > 0 and total_gifts["Porcelain Sculpture"] > 0) or (
        total_gifts["Gold"] > 0 and total_gifts["Diamond Jewellery"] > 0):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")
if materials:
    print(f"Materials left: {', '.join(map(str, materials))}")
if magic_levels:
    print(f"Magic left: {', '.join(map(str, magic_levels))}")

for key, value in total_gifts.items():
    if not value == 0:
        print(f"{key}: {value}")
