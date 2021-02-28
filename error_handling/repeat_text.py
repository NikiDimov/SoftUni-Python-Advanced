def repeat_text(text, times):
    return text * int(times)


text = "Hello"
times = "asd"

try:
    print(repeat_text(text, times))
except ValueError:
    print("The value must be an integer")
