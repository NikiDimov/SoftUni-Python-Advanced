n = input().split()
reverse_line = []
for index in range(len(n)):
    reverse_line.append(n.pop())
print(" ".join(reverse_line))
