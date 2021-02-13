def sorted_nums(nums):
    return list(map(int, sorted(nums, key=lambda x: int(x))))


nums = input().split()
print(sorted_nums(nums))
