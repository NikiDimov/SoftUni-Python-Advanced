from collections import deque

kids = deque(input().split())
n = int(input())
while len(kids) != 1:
    for _ in range(n):
        kids.append(kids.popleft())
    print(f"Removed {kids.pop()}")
print(f"Last is {kids[0]}")
