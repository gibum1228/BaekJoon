import sys
from collections import deque

IN = sys.stdin.readline

if __name__ == "__main__":
    N = int(IN())
    G = {k: [] for k in range(1, N+1)}
    in_degree = {k: 0 for k in range(1, N+1)}
    max_sec = {k: 0 for k in range(1, N+1)}
    results = {k: 0 for k in range(1, N+1)}

    # init graph
    for idx in range(1, N+1):
        arr = list(map(int, IN().split()))
        results[idx] =  arr[0]

        for end_idx in range(arr[1]):
            end = arr[2+end_idx]

            G[idx].append(end)
            in_degree[end] += 1

    # find no degree
    que = deque([])
    for idx in range(1, N+1):
        if in_degree[idx] == 0:
            que.append(idx)

    # search graph
    while que:
        node = que.popleft()

        for next_node in G[node]:
            in_degree[next_node] -= 1
            max_sec[next_node] = max(max_sec[next_node], results[node])

            if in_degree[next_node] == 0:
                que.append(next_node)
                results[next_node] += max_sec[next_node]

    print(max(results.values()))