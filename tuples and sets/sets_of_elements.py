numbers = input().split()
n = int(numbers[0])
m = int(numbers[1])
n_set = set()
m_set = set()
for _ in range(n):
    n_set.add(int(input()))
for _ in range(m):
    m_set.add(int(input()))
result = n_set.intersection(m_set)
for el in result:
    print(el)
    