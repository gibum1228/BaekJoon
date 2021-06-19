import sys
from collections import deque

N = int(sys.stdin.readline())
deque = deque()
result = ''

for i in range(N):
    order = sys.stdin.readline().split()

    if order[0] == 'push':
        deque.append(order[1])
    elif order[0] == 'pop':
        if not deque:
            result += '-1\n'
        else:
            result += str(deque.popleft()) + '\n'
    elif order[0] == 'size':
        result += str(len(deque)) + '\n'
    elif order[0] == 'empty':
        if not deque:
            result += '1\n'
        else:
            result += '0\n'
    elif order[0] == 'front':
        if not deque:
            result += '-1\n'
        else:
            result += str(deque[0]) + '\n'
    elif order[0] == 'back':
        if not deque:
            result += '-1\n'
        else:
            result += str(deque[-1]) + '\n'

print(result)