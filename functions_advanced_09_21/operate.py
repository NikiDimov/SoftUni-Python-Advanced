from functools import reduce


def operate(operator, *args):
    result = reduce(lambda x, y: eval(f"{x}{operator}{y}"), args)
    return result


print(operate('*', 3, 4))
