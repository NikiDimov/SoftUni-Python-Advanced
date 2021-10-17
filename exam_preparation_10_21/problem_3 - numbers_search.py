def numbers_searching(*args):
    duplicates = set([el for el in args if args.count(el) > 1])
    sorted_duplicates = sorted(duplicates)
    sorted_args = sorted(args)
    total_range = [i for i in range(sorted_args[0], sorted_args[-1] + 1)]
    last_missing_number = sorted(set(total_range).difference(sorted_args))[-1]
    return [last_missing_number, sorted_duplicates]


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
