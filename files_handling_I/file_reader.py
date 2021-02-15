with open("numbers.txt", "r") as file:
    sums = 0
    for el in file:
        sums += int(el)
print(sums)



