N = int(input())
even_numbers = set()
odd_numbers = set()
for i in range(1, N + 1):
    name = input()
    current_sum = 0
    for el in name:
        current_sum += ord(el)
    current_sum //= i
    if current_sum % 2 == 0:
        even_numbers.add(current_sum)
    else:
        odd_numbers.add(current_sum)
if sum(even_numbers) == sum(odd_numbers):
    print(*even_numbers.union(odd_numbers), sep=', ')
elif sum(odd_numbers) > sum(even_numbers):
    print(*odd_numbers.difference(even_numbers), sep=', ')
else:
    print(*odd_numbers.symmetric_difference(even_numbers), sep=', ')

