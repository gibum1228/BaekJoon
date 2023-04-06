import sys
from collections import deque

IN = sys.stdin.readline

if __name__ == "__main__":
    N = int(IN())
    graph = list(map(int, IN().split()))
    visited = [False for _ in range(len(graph))]
    visited[0] = True
    que = deque([(0, 0)])
    result = -1

    while que:
        idx, count = que.popleft()

        if idx >= len(graph) - 1:
            result = count
            break

        for i in range(1, graph[idx]+1):
            next_idx = idx + i

            if next_idx < len(graph) and not visited[next_idx]:
                visited[next_idx] = True
                que.append((next_idx, count + 1))

    print(result)