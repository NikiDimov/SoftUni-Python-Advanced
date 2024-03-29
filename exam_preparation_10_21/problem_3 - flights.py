def flights(*args):
    flight_dict = {}
    for i in range(len(args)):
        if args[i] == 'Finish':
            return flight_dict
        if i % 2 == 0:
            key = args[i]
            if key not in flight_dict:
                flight_dict[key] = 0
            flight_dict[key] += args[i + 1]
    return flight_dict


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
