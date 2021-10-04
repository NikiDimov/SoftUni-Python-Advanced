text = input()
try:
    times_to_repeat = int(input())
    result = ''
    for i in range(times_to_repeat):
        result += text
    print(result)
except ValueError:
    print("Variable times must be an integer")
