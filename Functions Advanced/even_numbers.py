def even_nums(nums):
    return list(map(int, filter(lambda x: int(x) % 2 == 0, nums)))


nums = input().split()
print(even_nums(nums))
