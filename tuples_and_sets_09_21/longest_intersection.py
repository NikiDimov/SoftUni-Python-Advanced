N = int(input())
current_intersection = set()


def checker(start, end):
    my_list = []
    for i in range(start, end + 1):
        my_list.append(i)
    return my_list


for _ in range(N):
    left, right = input().split("-")
    left_tuple = set()
    right_tuple = set()
    start_point, end_point = [int(el) for el in left.split(',')]
    left_tuple.update(checker(start_point, end_point))
    start_point2, end_point2 = [int(el) for el in right.split(',')]
    right_tuple.update(checker(start_point2, end_point2))
    intersection = left_tuple.intersection(right_tuple)
    if len(intersection) > len(current_intersection):
        current_intersection = intersection
print(f"Longest intersection is [{', '.join(map(str,current_intersection))}] with length {len(current_intersection)}")
