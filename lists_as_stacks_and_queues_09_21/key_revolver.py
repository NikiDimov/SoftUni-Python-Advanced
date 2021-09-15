from collections import deque
price_of_bullet = int(input())
size_of_a_gun_barrel = int(input())
bullets = [int(el)for el in input().split()]
locks = deque(int(el)for el in input().split())
value = int(input())
bullets_counter = 0

while locks:
    if not bullets:
        break
    current_shots = 0
    for _ in range(size_of_a_gun_barrel):
        if bullets and locks:
            bullets_counter += 1
            current_shots += 1
            if bullets.pop() <= locks[0]:
                locks.popleft()
                print('Bang!')
            else:
                print('Ping!')
    if bullets and current_shots == size_of_a_gun_barrel:
        print("Reloading!")
if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    bullets_cost = bullets_counter*price_of_bullet
    print(f"{len(bullets)} bullets left. Earned ${value-bullets_cost}")
