from collections import deque

firework = deque(int(el) for el in input().split(', '))
explosion = [int(el) for el in input().split(', ')]

palm, willow, crossette = 0, 0, 0
mission_complete = False

while firework and explosion:
    if firework[0] <= 0:
        firework.popleft()
        continue
    if explosion[-1] <= 0:
        explosion.pop()
        continue
    current_sum = firework[0] + explosion[-1]
    if current_sum % 3 == 0 and not current_sum % 5 == 0:
        palm += 1
        firework.popleft()
        explosion.pop()
    elif current_sum % 5 == 0 and not current_sum % 3 == 0:
        willow += 1
        firework.popleft()
        explosion.pop()
    elif current_sum % 3 == 0 and current_sum % 5 == 0:
        crossette += 1
        firework.popleft()
        explosion.pop()
    else:
        firework[0] -= 1
        firework.append(firework.popleft())
    if palm >= 3 and willow >= 3 and crossette >= 3:
        print("Congrats! You made the perfect firework show!")
        mission_complete = True
        break
if not mission_complete:
    print("Sorry. You can't make the perfect firework show.")
if firework:
    print(f"Firework Effects left: {', '.join(map(str, firework))}")
if explosion:
    print(f"Explosive Power left: {', '.join(map(str, explosion))}")
print(f"Palm Fireworks: {palm}\nWillow Fireworks: {willow}\nCrossette Fireworks: {crossette}")
