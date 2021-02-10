def concatenate(*args):
    return ''.join(filter(lambda x: x + x, args))


print(concatenate("Soft", "Uni", "Is", "Great", "!"))
