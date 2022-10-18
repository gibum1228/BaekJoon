import sys
from collections import deque

IN = sys.stdin.readline

if __name__ == "__main__":
    n = int(IN())
    a, b = map(int, IN().split())
    m = int(IN())
    G = {i: set() for i in range(1, n + 1)}

    # input
    for _ in range(m):
        x, y = map(int, IN().split())

        G[x].add(y)
        G[y].add(x)

    def bfs(start, end):
        que = deque([(start, 0)])
        visited = [False for _ in range(n+1)]
        visited[start] = True

        while que:
            current_node, current_count = que.popleft()

            if current_node == end:
                return current_count

            for next_node in G[current_node]:
                if not visited[next_node]:
                    visited[next_node] = True
                    que.append((next_node, current_count + 1))

        return -1

    result = max(bfs(a, b), bfs(b, a))
    print(result if result else -1)