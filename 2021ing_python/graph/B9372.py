import sys
from collections import deque

IN = sys.stdin.readline

if __name__ == "__main__":
    for _ in range(int(IN())):
        N, M = map(int, IN().split())
        G = {i: set() for i in range(1, N+1)}

        for __ in range(M):
            a, b = map(int, IN().split())

            G[a].add(b)
            G[b].add(a)

        count = 0
        visited = [False for __ in range(N+1)]
        que = deque([1])
        visited[1] = True
        while que:
            current_node = que.popleft()

            for next_node in G[current_node]:
                if not visited[next_node]:
                    visited[next_node] = True
                    que.append(next_node)
                    count += 1

        print(count)