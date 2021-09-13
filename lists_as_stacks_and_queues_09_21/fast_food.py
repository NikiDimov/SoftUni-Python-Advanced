from collections import deque

quantity = int(input())
order = deque([int(el) for el in input().split()])
order_complete = True
print(max(order))
while order:
    if order[0] <= quantity:
        quantity -= order.popleft()
    else:
        order_complete = False
        print(f"Orders left: {' '.join(map(str,order))}")
        break
if order_complete:
    print(f"Orders complete")
    