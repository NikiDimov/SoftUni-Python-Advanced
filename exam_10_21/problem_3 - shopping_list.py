def shopping_list(budget, **kwargs):
    result = []
    if budget < 100:
        return "You do not have enough budget."
    for key, value in kwargs.items():
        total = value[0] * value[1]
        if len(result) == 5:
            return '\n'.join(result)
        if total <= budget:
            budget -= total
            result.append(f"You bought {key} for {total:.2f} leva.")
    return '\n'.join(result)


print(shopping_list(100, microwave=(70, 2), skirts=(15, 4), coffee=(1.50, 10)))
print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))
print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
