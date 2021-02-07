def rounding(nums):
    nums = list(map(lambda x: round(x), nums))
    return nums


numbers = map(lambda x: float(x), input().split())
print(rounding(numbers))
