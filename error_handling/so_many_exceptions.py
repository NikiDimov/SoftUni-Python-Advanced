# input: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
# result: 0.003968253968253968
# Wrong Code:
# numbers_list = input().split(", ")
# result = 0
# for i in range(numbers_list):
#     number = numbers_list[i+1]
#     if number < 5:
#         result *= number
#     elif number > 5 and number > 10:
#         result /= number
# print(result)

# Fixed Code:

numbers_list = [int(num) for num in input().split(", ")]
result = 1
for num in numbers_list:
    if num <= 5:
        result *= num
    elif 5 < num <= 10:
        result /= num
print(result)
