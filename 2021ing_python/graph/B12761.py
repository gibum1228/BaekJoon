import sys
from collections import deque

IN = sys.stdin.readline

if __name__ == "__main__":
    A, B, N, M = map(int, IN().split())
    visited = [False for _ in range(100001)]

    que = deque([(N, 0)])
    visited[N] = True

    while que:
        position, distance = que.popleft()

        if position == M:
            print(distance)
            break

        for x in [1, -1, A, -A, B, -B]:
            dx = position + x
            if 0 <= dx < 100001 and not visited[dx]:
                que.append((dx, distance + 1))
                visited[dx] = True

        for x in [A, B]:
            dx = position * x
            if 0 <= dx < 100001 and not visited[dx]:
                que.append((dx, distance + 1))
                visited[dx] = True