class ValueCannotBeNegativeError(Exception):
    """Number is bellow Zero"""
    pass


for _ in range(5):
    num = int(input())
    if num < 0:
        raise ValueCannotBeNegativeError
