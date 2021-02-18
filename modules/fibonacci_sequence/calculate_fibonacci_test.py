from advanced.modules.fibonacci_sequence.calculate_fibonacci import create_sequence, locate_number

command = input()
while not command == "Stop":
    text = command.split()
    if text[0] == "Create":
        count = int(text[2])
        result = create_sequence(count)
        print(" ".join(map(str, result)))
    elif text[0] == "Locate":
        number = int(text[1])
        location = locate_number(number)
        if location is not None:
            print(f"The number - {number} is at index {location}")
        else:
            print(f"The number {number} is not in the sequence")

    command = input()
