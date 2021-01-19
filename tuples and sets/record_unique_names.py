n = int(input())
names = []
for _ in range(n):
    names.append(input())
for el in set(names):
    print(el)