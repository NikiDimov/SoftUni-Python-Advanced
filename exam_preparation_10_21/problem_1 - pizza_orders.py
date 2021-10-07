from collections import deque

pizza_orders = deque(int(pizza) for pizza in input().split(', '))
employee_capacity = [int(c) for c in input().split(', ')]

total_pizzas = 0

while pizza_orders and employee_capacity:
    if pizza_orders[0] not in range(1, 11):
        pizza_orders.popleft()
        continue
    if pizza_orders[0] <= employee_capacity[-1]:
        total_pizzas += pizza_orders.popleft()
        employee_capacity.pop()
    else:
        pizza_orders[0] -= employee_capacity[-1]
        total_pizzas += employee_capacity[-1]
        employee_capacity.pop()

if not pizza_orders:
    print(f"All orders are successfully completed!\nTotal pizzas made: {total_pizzas}")
    print(f"Employees: {', '.join(map(str,employee_capacity))}")
elif pizza_orders and not employee_capacity:
    print(f"Not all orders are completed.")
    print(f"Orders left: {', '.join(map(str, pizza_orders))}")


