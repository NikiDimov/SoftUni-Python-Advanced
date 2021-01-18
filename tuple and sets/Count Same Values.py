# Version 1
# numbers = [float(el)for el in input().split()]
# result = []
# for el in numbers:
#     text = f"{el} - {numbers.count(el)} times"
#     if text not in result:
#         result.append(text)
#
# print('\n'.join(result))

# Version 2
numbers = [float(el) for el in input().split()]
result = {}
for el in numbers:
    if el not in result:
        result[el] = numbers.count(el)
for key, value in result.items():
    print(f"{key} - {value} times")
