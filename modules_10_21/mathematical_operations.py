operation = input()

if '^' in operation:
    operation = operation.replace('^', '**')
print(f"{eval(operation):.2f}")
