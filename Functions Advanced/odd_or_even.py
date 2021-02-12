def odd_or_even(nums, command):
    if command == "Odd":
        return sum(filter(lambda x: x % 2 == 1, nums)) * len(nums)
    elif command == "Even":
        return sum(filter(lambda x: x % 2 == 0, nums)) * len(nums)


command = input()
nums = list(map(int, input().split()))
print(odd_or_even(nums, command))
