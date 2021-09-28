def fill_the_box(height, length, width, *args):
    box = height * length * width
    cubes = list(args[:args.index("Finish")])
    while cubes:
        if box == 0:
            break
        if cubes[0] <= box:
            box -= cubes.pop(0)
        else:
            cubes[0] -= box
            box = 0
    if box == 0:
        return f"No more free space! You have {sum(cubes)} more cubes."
    return f"There is free space in the box. You could put {box} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
