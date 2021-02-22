test = ([1, 2, 3, 4, 5], 10)


def best_list_pureness(*t):
    rotations = {}
    for i in range(t[1] + 1):
        sums = 0
        for j in range(len(t[0])):
            sums += t[0][j] * j
        rotations[i] = sums
        a = t[0].pop()
        t[0].insert(0, a)
    for key, value in rotations.items():
        if value == max(rotations.values()):
            return f"Best pureness {value} after {key} rotations"


result = best_list_pureness(*test)
print(result)
