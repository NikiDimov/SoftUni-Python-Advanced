stack = []
reversed_stack = []
N = int(input())
for _ in range(N):
    query = input()
    if query.startswith('1'):
        number = query.split()[1]
        stack.append(int(number))
    elif query.startswith('2'):
        if stack:
            stack.pop()
    elif query.startswith('3'):
        if stack:
            print(max(stack))
    elif query.startswith('4'):
        if stack:
            print(min(stack))
while stack:
    reversed_stack.append(stack.pop())
print(*reversed_stack, sep=', ')

