first_set, second_set = [int(el)for el in input().split()]
n = set()
m = set()
for _ in range(first_set):
    n.add(input())
for _ in range(second_set):
    m.add(input())
result = n & m
for el in result:
    print(el)
