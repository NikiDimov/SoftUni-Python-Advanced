result = {"Positive": [], "Negative": [], "Even": [], "Odd": []}
numbers = input().split(", ")
[result["Positive"].append(int(el)) if int(el) >= 0 else result["Negative"].append(int(el)) for el in numbers]
[result["Even"].append(int(el)) if int(el) % 2 == 0 else result["Odd"].append(int(el)) for el in numbers]
[print(f"{key}: {', '.join(map(str, value))}")for key, value in result.items()]

