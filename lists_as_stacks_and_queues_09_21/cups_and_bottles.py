from collections import deque

cups = deque(int(el) for el in input().split())
bottles = [int(el) for el in input().split()]
wasted_water = 0

while cups:
    if not bottles:
        break
    current_cup = cups[0]
    current_bottle = bottles.pop()
    if current_cup <= current_bottle:
        cups.popleft()
        wasted_water += current_bottle - current_cup
    else:
        cups[0] -= current_bottle
if not cups:
    print(f"Bottles: {' '.join(map(str, bottles))}")
else:
    print(f"Cups: {' '.join(map(str, cups))}")
print(f"Wasted litters of water: {wasted_water}")
