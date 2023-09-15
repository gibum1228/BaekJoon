import sys
from collections import deque

IN = sys.stdin.readline

if __name__ == "__main__":
    N = int(IN())
    G = {k: [] for k in range(1, N+1)}
    in_degree = [0 for _ in range(N+1)]
    results = {k: 0 for k in range(1, N+1)}
    max_sec = {k: 0 for k in range(1, N+1)}

    # input info
    for start in range(1, N+1):
        arr = list(map(int, IN().split()))

        results[start] += arr[0]

        for end_idx in range(1, len(arr)-1):
            end = arr[end_idx]
            G[end].append(start)
            in_degree[start] += 1

    # init que
    que = deque([])
    for i in range(1, N+1):
        if in_degree[i] == 0:
            que.append(i)

    # graph search
    while que:
        node = que.popleft()

        for next_node in G[node]:
            in_degree[next_node] -= 1
            max_sec[next_node] = max(max_sec[next_node], results[node])

            if in_degree[next_node] <= 0:
                que.append(next_node)
                results[next_node] += max_sec[next_node]

    # print
    for k, v in results.items():
        print(v)