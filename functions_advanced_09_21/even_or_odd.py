def even_odd(*args):
    result = []
    if args[-1] == 'even':
        result = [el for el in args[:-1] if el % 2 == 0]
    elif args[-1] == 'odd':
        result = [el for el in args[:-1] if el % 2 == 1]
    return result


print(even_odd(1, 2, 3, 4, 5, 6, 'even'))
