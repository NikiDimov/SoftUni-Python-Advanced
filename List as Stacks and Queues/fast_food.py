from collections import deque

food_quantity = int(input())
orders = input().split()
orders = [int(el) for el in orders]
orders = deque(orders)
print(max(orders))
for index in range(len(orders)):
    if orders[0] <= food_quantity:
        current_food = orders.popleft()
        food_quantity -= current_food
    else:
        break
orders = " ".join(map(str, orders))
if len(orders) > 0:
    print(f"Orders left: {orders}")
else:
    print("Orders complete")
    