import sys
from collections import deque

IN = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, IN().split())
    G = {k: [] for k in range(1, N+1)}
    in_degree = {k: 0 for k in range(1, N+1)}

    # init graph
    for _ in range(M):
        arr = list(map(int, IN().split()))

        for i in range(2, len(arr)):
            start, end = arr[i-1], arr[i]

            G[start].append(end)
            in_degree[end] += 1

    # find no in_degree
    que = deque([])
    for i in range(1, N+1):
        if in_degree[i] == 0:
            que.append(i)

    # search graph
    result = []
    if que:
        while que:
            node = que.popleft()
            result.append(str(node))

            for next_node in G[node]:
                in_degree[next_node] -= 1

                if in_degree[next_node] == 0:
                    que.append(next_node)
                elif in_degree[next_node] < 0:
                    que = []
                    break

        print('\n'.join(result) if len(result) == N else 0)
    else: # que가 비어 있으면 사이클인 그래프
        print(0)