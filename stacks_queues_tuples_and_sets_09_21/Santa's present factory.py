from collections import deque

presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}
crafted_presents = {}
materials = [int(el) for el in input().split()]
magic = deque(int(el) for el in input().split())

while materials and magic:
    current_material = materials[-1]
    current_magic = magic[0]
    total_level = current_magic * current_material
    if total_level in presents:
        current_material = materials.pop()
        current_magic = magic.popleft()
        present = presents[total_level]
        if present not in crafted_presents:
            crafted_presents[present] = 0
        crafted_presents[present] += 1
    elif total_level < 0:
        result = current_magic + current_material
        current_material = materials.pop()
        current_magic = magic.popleft()
        materials.append(result)
    elif total_level > 0:
        magic.popleft()
        materials[-1] += 15
    elif total_level == 0:
        if current_material == 0:
            materials.pop()
        if current_magic == 0:
            magic.popleft()
if ("Doll" in crafted_presents and "Wooden train" in crafted_presents) or \
        ("Teddy bear" in crafted_presents and "Bicycle" in crafted_presents):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials:
    print(f"Materials left: {', '.join(map(str, materials[::-1]))}")
if magic:
    print(f"Magic left: {', '.join(map(str, magic))}")
for key, value in sorted(crafted_presents.items()):
    print(f"{key}: {value}")
