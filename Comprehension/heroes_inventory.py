heroes_dict = {hero: {} for hero in input().split(", ")}
command = input()
while not command == "End":
    hero, item, cost = command.split("-")
    cost = int(cost)
    if item not in heroes_dict[hero]:
        heroes_dict[hero][item] = cost
    command = input()
print(*[f"{name} -> Items: {len(inventory)}, Cost: {sum(inventory.values())}"
        for name, inventory in heroes_dict.items()], sep="\n")
