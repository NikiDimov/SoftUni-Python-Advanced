def even_odd(*args):
    result = list(filter(lambda x: x, args))
    if "even" in result:
        result.remove("even")
        return list(filter(lambda x: x % 2 == 0, result))
    elif "odd" in result:
        result.remove("odd")
        return list(filter(lambda x: x % 2 == 1, result))


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
