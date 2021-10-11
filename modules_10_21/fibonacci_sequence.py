from modules.fibonacii_sequence.fibonacii import fibonacci, locate_a_number

command = input()
current_sequence = []
while not command == "Stop":
    data = command.split()
    if data[0] == 'Create':
        N = int(data[2])
        current_sequence = fibonacci(N)
        if current_sequence:
            print(f"{' '.join(map(str,current_sequence))}")
    elif data[0] == 'Locate':
        if current_sequence:
            K = int(data[1])
            print(locate_a_number(K, current_sequence))

    command = input()
