line = [int(el) for el in input().split()]
negative_nums = [el for el in line if el < 0]
positive_nums = [el for el in line if el > 0]
print(sum(negative_nums))
print(sum(positive_nums))
if abs(sum(negative_nums)) > abs(sum(positive_nums)):
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
