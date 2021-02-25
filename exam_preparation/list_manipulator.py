def list_manipulator(lists, com_1, com_2, *args):
    if com_1 == "add" and com_2 == "beginning":
        return [*args] + lists
    elif com_1 == "add" and com_2 == "end":
        return lists + [*args]
    elif com_1 == "remove" and com_2 == "beginning":
        if args:
            for _ in range(args[0]):
                lists.remove(lists[0])
        else:
            lists.remove(lists[0])
        return lists
    elif com_1 == "remove" and com_2 == "end":
        if args:
            for _ in range(args[0]):
                lists.pop()
        else:
            lists.pop()
        return lists


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))