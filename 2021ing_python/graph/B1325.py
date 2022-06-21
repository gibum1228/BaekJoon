import sys
from collections import deque

IN = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, IN().split())
    G = [[] for _ in range(N+1)]
    results = [0 for _ in range(N+1)]
    max_count = 0

    # input
    for _ in range(M):
        A, B = map(int, IN().split())
        G[B].append(A)

    # bfs
    def bfs(i):
        visited = [False for _ in range(N+1)]
        visited[i] = True
        que = deque([i])
        depth = 1

        while que:
            x = que.popleft()

            for next_x in G[x]:
                if not visited[next_x]:
                    que.append(next_x)
                    visited[next_x] = True
                    depth += 1

        return depth

    # logic
    for i in range(1, N+1):
        results[i] = bfs(i)
        max_count = max(max_count, results[i])

    # print
    for i, r in enumerate(results):
        if max_count == r:
            print(i, end=" ")