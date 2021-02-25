from collections import deque
customers = [int(cust) for cust in input().split(", ")]
taxis = [int(t)for t in input().split(", ")]
customers = deque(customers)
total_time = 0
while not len(taxis) == 0:
    if taxis[-1] >= customers[0]:
        total_time += customers[0]
        customers.popleft()
        taxis.pop()
    else:
        taxis.pop()
if len(customers) == 0:
    print(f"All customers were driven to their destinations\nTotal time: {total_time} minutes")
else:
    print(f"Not all customers were driven to their destinations\nCustomers left: {', '.join(map(str,customers))}")
