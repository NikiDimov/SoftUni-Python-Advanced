n = int(input())
first_set = set()
second_set = set()
longest_intersection = set()
for _ in range(n):
    t1, t2 = input().split("-")
    tuple1 = tuple(map(int, t1.split(",")))
    tuple2 = tuple(map(int, t2.split(",")))
    for i in range(tuple1[0], tuple1[1] + 1):
        first_set.add(i)
    for i in range(tuple2[0], tuple2[1] + 1):
        second_set.add(i)
    current_intersection = first_set.intersection(second_set)
    if len(current_intersection) > len(longest_intersection):
        longest_intersection = current_intersection
    first_set = set()
    second_set = set()
print(f"Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}")
