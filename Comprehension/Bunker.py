bunker = {el: {} for el in input().split(", ")}
quan = 0
sum_quals = 0
for _ in range(int(input())):
    command = input().split(" - ")
    quantity, quality = command[2].split(";")
    quan += int(quantity.split(":")[1])
    qual = int(quality.split(":")[1])
    bunker[command[0]][command[1]] = qual
print(f"Count of items: {quan}")
for key, value in bunker.items():
    sum_quals += sum(value.values())
print(f"Average quality: {sum_quals / len(bunker):.2f}")
print(*[f"{key} -> {', '.join(list(value.keys()))}" for key, value in bunker.items()], sep="\n")
