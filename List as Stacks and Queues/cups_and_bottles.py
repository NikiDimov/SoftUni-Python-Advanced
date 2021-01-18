from collections import deque

cups = [int(el) for el in input().split()]
bottles = [int(el) for el in input().split()]
cups = deque(cups)
wasted = 0

while len(bottles) > 0:
    if len(cups) == 0:
        bottles = bottles[::-1]
        print(f"Bottles: {' '.join(map(str, bottles))}")
        print(f"Wasted litters of water: {wasted}")
        break
    current_bottle = bottles.pop()
    current_cup = cups[0]
    if current_bottle >= current_cup:
        wasted += current_bottle - current_cup
        cups.popleft()
    else:
        current_cup -= current_bottle
        cups[0] = current_cup

if len(cups) > 0:
    print(f"Cups: {' '.join(map(str, cups))}")
    print(f"Wasted litters of water: {wasted}")
