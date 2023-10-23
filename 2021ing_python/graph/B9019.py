import sys
from collections import deque

IN = sys.stdin.readline

if __name__ == "__main__":
    T = int(IN())
    result = ""
    for _ in range(T):
        A, B = map(int, IN().split())
        visited = {A}
        que = deque([(A, "")])

        while que:
            n, logics = que.popleft()

            for order in ['D', 'S', 'L', 'R']:
                if order == 'D':
                    next_num = (n * 2) % 10000
                elif order == 'S':
                    next_num = n - 1 if n != 0 else 9999
                elif order == 'L':
                    next_num = (n % 1000 * 10) + (n // 1000)
                elif order == 'R':
                    next_num = (n % 10 * 1000) + (n // 10)

                if next_num == B:
                    result += logics + order + "\n"
                    que = False
                    break
                else:
                    if next_num not in visited:
                        que.append((next_num, logics + order))
                        visited.add(next_num)

    print(result)