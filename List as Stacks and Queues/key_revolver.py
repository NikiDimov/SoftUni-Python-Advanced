from collections import deque

bullet_price = int(input())
size_barrel = int(input())
initial_size_barrel = size_barrel
bullets = [int(el) for el in input().split()]
locks = [int(el) for el in input().split()]
value_of_intelligence = int(input())
money_earned = value_of_intelligence
locks = deque(locks)
counter_bullets = 0
while len(bullets) > 0:
    current_bullet = bullets.pop()
    counter_bullets += 1
    current_lock = locks[0]
    if current_bullet <= current_lock:
        print("Bang!")
        locks.popleft()
    else:
        print("Ping!")
    size_barrel -= 1
    if size_barrel == 0 and len(bullets):
        print("Reloading!")
        size_barrel = initial_size_barrel
    money_earned -= bullet_price
    if len(locks) == 0:
        print(f"{len(bullets)} bullets left. Earned ${money_earned}")
        break
if len(locks) > 0:
    print(f"Couldn't get through. Locks left: {len(locks)}")
