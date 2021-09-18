from collections import deque
from math import floor

expression = input().split()
current_result = ''
operators = ['-', '+', '*', '/']
my_queue = deque()
for el in expression:
    if el not in operators:
        my_queue.append(int(el))
    else:
        if el == '-':
            if not current_result:
                current_result = my_queue.popleft()
            while my_queue:
                current_result -= my_queue.popleft()
        elif el == '/':
            if not current_result:
                current_result = my_queue.popleft()
            while my_queue:
                current_result /= my_queue.popleft()
                current_result = floor(current_result)
        elif el == '*':
            if not current_result:
                current_result = 1
            while my_queue:
                current_result *= my_queue.popleft()
        elif el == '+':
            if not current_result:
                current_result = 0
            while my_queue:
                current_result += my_queue.popleft()
print(current_result)
