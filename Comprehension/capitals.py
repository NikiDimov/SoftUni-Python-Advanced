countries = input().split(", ")
capitals = input().split(", ")
result = {el[0]: el[1] for el in tuple(zip(countries, capitals))}
for country, capital in result.items():
    print(f"{country} -> {capital}")
