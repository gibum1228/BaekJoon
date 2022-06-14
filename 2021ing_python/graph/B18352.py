import sys
from collections import deque

IN = sys.stdin.readline

if __name__ == "__main__":
    N, M, K, X = map(int, IN().split())
    G = [[] for _ in range(N+1)]
    distance = [N + 1 for _ in range(N+1)]
    distance[0], distance[X] = -1, 0

    # input data
    for _ in range(M):
        A, B = map(int, IN().split())
        G[A].append(B)

    # dijkstra
    q = deque([X])
    while q:
        x = q.popleft()

        for g in G[x]:
            if distance[x] + 1 < distance[g]:
                distance[g] = distance[x] + 1
                q.append(g)

    result = ""
    for i, node in enumerate(distance):
        if node == K:
            result += f"{i}\n"

    print(result) if result != "" else print(-1)