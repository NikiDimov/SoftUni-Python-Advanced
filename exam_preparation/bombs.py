from collections import deque


def check_bomb_effects(b_eff):
    if b_eff:
        return f"Bomb Effects: {', '.join(map(str, b_eff))}"
    return "Bomb Effects: empty"


def check_bomb_casing(b_case):
    if b_case:
        return f"Bomb Casings: {', '.join(map(str, b_case))}"
    return "Bomb Casings: empty"


bombs = {"Cherry Bombs": 0, "Datura Bombs": 0, "Smoke Decoy Bombs": 0}
bomb_effects = [int(el) for el in input().split(", ")]
bomb_casing = [int(el) for el in input().split(", ")]
bomb_effects = deque(bomb_effects)
while bomb_effects and bomb_casing:
    if bomb_effects[0] + bomb_casing[-1] == 40:
        bombs["Datura Bombs"] += 1
        bomb_effects.popleft()
        bomb_casing.pop()
    elif bomb_effects[0] + bomb_casing[-1] == 60:
        bombs["Cherry Bombs"] += 1
        bomb_effects.popleft()
        bomb_casing.pop()
    elif bomb_effects[0] + bomb_casing[-1] == 120:
        bombs["Smoke Decoy Bombs"] += 1
        bomb_effects.popleft()
        bomb_casing.pop()
    else:
        bomb_casing[-1] -= 5
    if bombs["Datura Bombs"] >= 3 and bombs["Cherry Bombs"] >= 3 and bombs["Smoke Decoy Bombs"] >= 3:
        print("Bene! You have successfully filled the bomb pouch!")
        break

if not (bombs["Datura Bombs"] >= 3 and bombs["Cherry Bombs"] >= 3 and bombs["Smoke Decoy Bombs"] >= 3):
    print("You don't have enough materials to fill the bomb pouch.")
print(check_bomb_effects(bomb_effects))
print(check_bomb_casing(bomb_casing))
for key, value in bombs.items():
    print(f"{key}: {value}")
    