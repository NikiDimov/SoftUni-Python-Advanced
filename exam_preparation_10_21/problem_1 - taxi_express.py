from collections import deque

customers = deque(int(el) for el in input().split(', '))
taxis = [int(el) for el in input().split(', ')]

total_time = 0

while customers and taxis:
    if customers[0] <= taxis[-1]:
        total_time += customers.popleft()
        taxis.pop()
    else:
        taxis.pop()

if not customers:
    print(f"All customers were driven to their destinations\nTotal time: {total_time} minutes")
if not taxis and customers:
    print(f"Not all customers were driven to their destinations\nCustomers left: {', '.join(map(str,customers))}")
