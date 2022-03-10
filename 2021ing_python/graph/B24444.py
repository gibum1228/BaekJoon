import sys
from unittest import result

IN = sys.stdin.readline

def bfs(start):
    que = [start]
    visited[start] = True
    results[start] = 1
    count = 2

    while que:
        focus_node = que.pop(0)

        for next_node in G[focus_node]:
            if not visited[next_node]:
                visited[next_node] = True
                que.append(next_node)
                results[next_node] = count
                count += 1

if __name__ == "__main__":
    N, M, R = map(int, IN().split())
    G = [[] for _ in range(N+1)]
    visited = [False for _ in range(N+1)]
    results = [0 for _ in range(N+1)]

    for _ in range(M):
        u, v = map(int, IN().split())

        G[u].append(v)
        G[v].append(u)
    
    for i in range(1, N+1):
        G[i].sort()

    bfs(R)

    print("\n".join(map(str, results[1:])))