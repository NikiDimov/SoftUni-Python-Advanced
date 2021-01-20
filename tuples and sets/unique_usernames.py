n = int(input())
unique_user_names = set()
for _ in range(n):
    user_name = input()
    unique_user_names.add(user_name)
for el in unique_user_names:
    print(el)
