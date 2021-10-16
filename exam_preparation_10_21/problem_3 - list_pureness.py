from collections import deque


def best_list_pureness(*test):
    numbers = deque(test[0])
    rotations = test[1]
    best_pureness = 0
    rotation = 0
    for r in range(rotations+1):
        current_pureness = 0
        for el in numbers:
            current_pureness += el * numbers.index(el)
        if current_pureness > best_pureness:
            best_pureness = current_pureness
            rotation = r
        numbers.appendleft(numbers.pop())
    return f"Best pureness {best_pureness} after {rotation} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)
test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)
test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)

