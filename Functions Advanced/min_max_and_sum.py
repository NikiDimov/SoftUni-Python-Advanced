def min_max_sum(nums):
    return f"The minimum number is {min(nums)}\nThe maximum number is {max(nums)}\nThe sum number is: {sum(nums)}"


nums = list(map(int, input().split()))
print(min_max_sum(nums))
