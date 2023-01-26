import sys
from collections import deque

IN = sys.stdin.readline

if __name__ == "__main__":
    N, K = map(int, IN().split())
    G = {k:[] for k in range(1, N+1)}

    # input Graph
    for _ in range(K):
        A, B = map(int, IN().split())

        G[A].append(B)
        G[B].append(A)

    def bfs(start_node):
        que = deque([(start_node, 0)])
        visited = set()
        visited.add(start_node)

        while que:
            node, dist = que.popleft()
            if dist > 6: return False

            for next_node in G[node]:
                if next_node not in visited:
                    visited.add(next_node)
                    que.append((next_node, dist+1))

        return True if len(visited) == N else False # if small world then True else False

    result = True
    for i in range(1, N+1):
        if not bfs(i):
            result = False
            break

    print("Small World!" if result else "Big World!")