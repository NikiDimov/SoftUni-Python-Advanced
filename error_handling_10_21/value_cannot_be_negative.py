class ValueCannotBeNegative(Exception):
    """Number is bellow zero"""
    pass


for _ in range(5):
    num = int(input())
    if num < 0:
        raise ValueCannotBeNegative
