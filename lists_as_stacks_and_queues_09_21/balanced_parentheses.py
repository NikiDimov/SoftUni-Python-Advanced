mapper = {"{": "}", "(": ")", "[": "]"}
line = list(input())
stack = [line[0]]
for i in range(1, len(line)):
    if stack and stack[-1] in mapper and line[i] == mapper[stack[-1]]:
        stack.pop()
    else:
        stack.append(line[i])
if stack:
    print("NO")
else:
    print("YES")
