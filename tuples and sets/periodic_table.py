n = int(input())
set_of_elements = set()
for _ in range(n):
    chemicals = input().split()
    for el in chemicals:
        set_of_elements.add(el)
for el in set_of_elements:
    print(el)
    