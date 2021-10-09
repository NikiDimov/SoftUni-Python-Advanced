from collections import deque

males = [int(m) for m in input().split()]
females = deque(int(f) for f in input().split())
matches = 0

while males and females:
    last_male = males[-1]
    first_female = females[0]
    if last_male <= 0:
        males.pop()
        continue
    if first_female <= 0:
        females.popleft()
        continue
    if last_male % 25 == 0:
        males.pop()
        if males:
            males.pop()
        continue
    if first_female % 25 == 0:
        females.popleft()
        if females:
            females.popleft()
        continue
    if last_male == first_female:
        matches += 1
        males.pop()
        females.popleft()
    else:
        females.popleft()
        males[-1] -= 2

print(f"Matches: {matches}")
if not males:
    print("Males left: none")
else:
    print(f"Males left: {', '.join(map(str, males[::-1]))}")
if not females:
    print("Females left: none")
else:
    print(f"Females left: {', '.join(map(str, females))}")
