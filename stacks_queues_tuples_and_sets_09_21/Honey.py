from collections import deque
bees = deque(int(el)for el in input().split())
nectar = [int(el)for el in input().split()]
symbols = deque(input().split())
total_honey = 0
while bees and nectar:

    current_bee = bees[0]
    current_nectar = nectar.pop()
    if current_nectar >= current_bee:
        current_bee = bees.popleft()
        current_symbol = symbols.popleft()
        if current_symbol == '+':
            honey = current_bee + current_nectar
            total_honey += honey
        elif current_symbol == '-':
            honey = current_bee - current_nectar
            total_honey += abs(honey)
        elif current_symbol == '/':
            if not current_nectar == 0:
                honey = current_bee / current_nectar
                total_honey += honey
        elif current_symbol == '*':
            honey = current_bee * current_nectar
            total_honey += honey
print(f"Total honey made: {total_honey}")
if bees:
    print(f"Bees left: {', '.join(map(str, bees))}")
if nectar:
    print(f"Nectar left: {', '.join(map(str, nectar))}")


