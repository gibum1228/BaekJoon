import sys
from collections import deque

IN = sys.stdin.readline

if __name__ == "__main__":
    G = {i: set() for i in range(1, int(IN()) + 1)}

    for _ in range(int(IN())):
        a, b = map(int, IN().split())

        G[a].add(b)
        G[b].add(a)

    que = deque([(1, 0)])
    visited = [False for _ in range(len(G) + 1)]
    visited[1] = True
    count = 0

    while que:
        current_node, current_weight = que.popleft()

        if current_weight < 2:
            for next_node in G[current_node]:
                if not visited[next_node]:
                    visited[next_node] = True
                    que.append((next_node, current_weight + 1))
                    count += 1

    print(count)