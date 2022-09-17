import sys
from collections import deque

IN = sys.stdin.readline

if __name__ == "__main__":
    N, K = map(int, IN().split())
    G = [[] for _ in range(N+1)]

    for _ in range(K):
        A, B = map(int, IN().split())

        G[A].append(B)
        G[B].append(A)

    def bfs(start_node):
        result = 0
        que = deque([start_node])
        visited = [False for _ in range(N+1)]
        visited[start_node] = True

        while que:
            print(*que)
            node = que.popleft()

            for next_node in G[node]:
                if not visited[next_node]:
                    visited[next_node] = True
                    result += 1
                    que.append(next_node)

        return result

    print(bfs(1))