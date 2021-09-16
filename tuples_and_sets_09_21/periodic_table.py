n = int(input())
elements = set()
for _ in range(n):
    elements.update(input().split())
for el in elements:
    print(el)

