import sys
from collections import deque

IN = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, IN().split())
    G = [[] for _ in range(N + 1)]
    visited = [False for _ in range(N + 1)]

    for _ in range(M):
        A, B = map(int, IN().split())

        G[A].append(B)

    X = int(IN())
    result = 0

    def dfs(start, count):
        global result

        if start == X:
            result += count
            return

        for x in G[start]:
            if not visited[x]:
                 visited[x] = True
                 dfs(x, count + 1)
            else:
                dfs(x, count)

    for i in range(1, N+1):
        if G[i]:
            if not visited[i]:
                visited[i] = True
                dfs(i, 1)
            else:
                dfs(i, 0)

    print(result)