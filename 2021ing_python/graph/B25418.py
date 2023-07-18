import sys
from collections import deque

IN = sys.stdin.readline

if __name__ == "__main__":
    A, K = map(int, IN().split())
    que = deque([(A, 0)])
    visited = set([A])

    while que:
        x, sec = que.popleft()

        case_1 = x + 1
        case_2 = x * 2

        if case_1 == K or case_2 == K:
            print(sec + 1)
            break

        if 0 <= case_1 <= 1000000 and case_1 not in visited:
            que.append((case_1, sec + 1))
            visited.add(case_1)

        if 0 <= case_2 <= 1000000 and case_2 not in visited:
            que.append((case_2, sec + 1))
            visited.add(case_2)