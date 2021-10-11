def fibonacci(n):
    if n <= 0:
        return
    elif n == 1:
        result = [0]
    elif n == 2:
        result = [0, 1]
    elif n == 3:
        result = [0, 1, 1]
    else:
        result = [0, 1, 1, 2]
        for i in range(n - 4):
            result.append(sum(result[-2:]))
    return result


def locate_a_number(k, sequence):
    if k in sequence:
        return f"The number - {k} is at index {sequence.index(k)}"
    else:
        return f"The number {k} is not in the sequence"

