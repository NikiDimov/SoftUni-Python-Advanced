from collections import deque

chocolates = [int(el) for el in input().split(', ')]
cups_of_milk = deque(int(el) for el in input().split(', '))
shakes = 0
while shakes < 5:
    if not chocolates or not cups_of_milk:
        break
    if chocolates[-1] <= 0 and cups_of_milk[0] > 0:
        chocolates.pop()
        continue
    if cups_of_milk[0] <= 0 and chocolates[-1] > 0:
        cups_of_milk.popleft()
        continue
    if chocolates[-1] <= 0 and cups_of_milk[0] <= 0:
        chocolates.pop()
        cups_of_milk.popleft()
        continue
    if chocolates and cups_of_milk:
        if chocolates[-1] == cups_of_milk[0]:
            chocolates.pop()
            cups_of_milk.popleft()
            shakes += 1
        else:
            cups_of_milk.append(cups_of_milk.popleft())
            chocolates[-1] -= 5


if shakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolates:
    print(f"Chocolate: {', '.join(map(str, chocolates))}")
else:
    print("Chocolate: empty")
if cups_of_milk:
    print(f"Milk: {', '.join(map(str, cups_of_milk))}")
else:
    print("Milk: empty")
