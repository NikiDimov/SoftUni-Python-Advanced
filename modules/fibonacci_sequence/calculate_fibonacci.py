seq = []


def create_sequence(num):
    global seq
    if num == 1:
        seq = [0]
    elif num == 2:
        seq = [0, 1]
    elif num > 2:
        seq = [0, 1]
        for i in range(2, num):
            seq.append(seq[i - 2] + seq[i - 1])
    else:
        seq = []
    return seq


def locate_number(n):
    for el in seq:
        if el == n:
            return seq.index(el)
        else:
            return None

