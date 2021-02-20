from collections import deque


def special_case(people):
    for el in people.copy():
        if el % 25 == 0:
            people.remove(el)
    return people


def people_left(people):
    if len(people) > 0:
        return ", ".join(map(str, people))
    else:
        return "none"


males = special_case([int(m) for m in input().split() if not int(m) <= 0])
females = special_case([int(f) for f in input().split() if not int(f) <= 0])
females = deque(females)

matches = 0
while not (len(males) and len(females)) == 0:
    if males[-1] == females[0]:
        males.pop()
        females.popleft()
        matches += 1
    else:
        females.popleft()
        males[-1] = males[-1] - 2
        if males[-1] <= 0 or males[-1] % 25 == 0:
            males.pop()
print(f"Matches: {matches}")
print(f"Males left: {people_left(males[::-1])}")
print(f"Females left: {people_left(females)}")

