N = int(input())
unique_names = set()
for _ in range(N):
    name = input()
    unique_names.add(name)
for name in unique_names:
    print(name)