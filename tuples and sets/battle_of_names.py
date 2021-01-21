n = int(input())
odd = set()
even = set()
for i in range(1, n+1):
    name = input()
    sum_chars = 0
    for el in name:
        sum_chars += ord(el)
    sum_chars = sum_chars // i
    if sum_chars % 2 == 0:
        even.add(sum_chars)
    else:
        odd.add(sum_chars)
if sum(odd) == sum(even):
    print(', '.join(map(str, odd.union(even))))
elif sum(odd) > sum(even):
    print(', '.join(map(str, odd.difference(even))))
elif sum(even) > sum(odd):
    print(', '.join(map(str, even.symmetric_difference(odd))))
    