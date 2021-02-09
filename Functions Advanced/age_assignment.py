def age_assignment(*args, **kwargs):
    result = {}
    for name in args:
        for key, value in kwargs.items():
            if key == name[0]:
                result[name] = value

    return result


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
