from collections import deque

bomb_effects = deque(int(el) for el in input().split(', '))
bomb_casings = [int(el) for el in input().split(', ')]

bombs = {
    'Datura Bombs': 40,
    'Cherry Bombs': 60,
    'Smoke Decoy Bombs': 120,
}

bombs_pouch = {
    'Cherry Bombs': 0,
    'Datura Bombs': 0,
    'Smoke Decoy Bombs': 0,
}


def pouch():
    return bombs_pouch['Datura Bombs'] >= 3 and \
           bombs_pouch['Cherry Bombs'] >= 3 and \
           bombs_pouch['Smoke Decoy Bombs'] >= 3


def extract_key(total):
    for key, value in bombs.items():
        if value == total:
            bombs_pouch[key] += 1


while bomb_effects and bomb_casings and not pouch():
    current_sum = bomb_effects[0] + bomb_casings[-1]
    if current_sum in bombs.values():
        extract_key(current_sum)
        bomb_effects.popleft()
        bomb_casings.pop()
    else:
        bomb_casings[-1] -= 5

if pouch():
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")
if bomb_effects:
    print(f"Bomb Effects: {', '.join(map(str, bomb_effects))}")
else:
    print(f"Bomb Effects: empty")
if bomb_casings:
    print(f"Bomb Casings: {', '.join(map(str, bomb_casings))}")
else:
    print("Bomb Casings: empty")

for key, value in bombs_pouch.items():
    print(f"{key}: {value}")
