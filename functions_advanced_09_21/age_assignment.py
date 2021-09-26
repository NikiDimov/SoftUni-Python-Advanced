def age_assignment(*args, **kwargs):
    result = {}
    for key, value in kwargs.items():
        for name in args:
            if name[0] == key:
                result[name] = value
    return result


print(age_assignment('Nick', 'George', G=20, N=24))
