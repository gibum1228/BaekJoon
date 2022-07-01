import sys
from collections import deque

IN = sys.stdin.readline

if __name__ == "__main__":
    a, b = map(int, IN().split())
    N, M = map(int, IN().split())
    G = [[] for _ in range(N + 1)]
    visited = [False for _ in range(N+1)]

    # create graph
    for _ in range(M):
        start, end = map(int, IN().split())
        G[start].append(end)
        G[end].append(start)

    def bfs(start):
        que = deque([(start, 0)])

        while que:
            node, distance = que.popleft()
            if node == b:
                print(distance)
                return True

            for next_node in G[node]:
                if not visited[next_node]:
                    visited[next_node] = True
                    que.append((next_node, distance + 1))

        return False

    trigger = bfs(a)

    if not trigger:
        print(-1)