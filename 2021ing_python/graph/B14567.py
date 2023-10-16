import sys
from collections import deque

IN = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, IN().split())
    # 4 Byte * 1000 * 2 = 8000 Byte = 8 KB
    in_degree = [0 for _ in range(N)]
    G = {k: set() for k in range(N)} # 4 Byte * 5000000 = 2000000 KB = 2000MB
    results = [0 for _ in range(N)]

    # input
    for _ in range(M):
        A, B = map(int, IN().split())

        G[A-1].add(B-1)
        in_degree[B-1] += 1

    # find que
    que = deque()
    for idx in range(N):
        if in_degree[idx] == 0:
            que.append(idx)
            results[idx] = 1

    # sort
    while que:
        node = que.popleft()

        for next_node in G[node]:
            in_degree[next_node] -= 1

            if in_degree[next_node] == 0:
                results[next_node] = results[node] + 1
                que.append(next_node)

    # print
    print(*results)