from collections import deque
kids = input().split()
n = int(input())
kids = deque(kids)
counter = 0
while len(kids) > 1:
    counter += 1
    current_player = kids.popleft()
    if counter == n:
        print(f"Removed {current_player}")
        counter = 0
    else:
        kids.append(current_player)
print(f"Last is {kids[0]}")
