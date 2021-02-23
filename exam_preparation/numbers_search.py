def numbers_searching(*args):
    dict_nums = {}
    missing_num = 0
    duplicate_nums = []
    for el in args:
        if el not in dict_nums:
            dict_nums[el] = 1
        else:
            dict_nums[el] += 1
    for i in range(min(dict_nums), max(dict_nums) + 1):
        if i not in dict_nums:
            missing_num = i
    for key, value in dict_nums.items():
        if value > 1:
            duplicate_nums.append(key)
    return [missing_num, sorted(duplicate_nums)]


print(numbers_searching(1, 2, 4, 2, 5, 4))
