import sys
import heapq
sys.setrecursionlimit(10**6)

IN = sys.stdin.readline

if __name__ == "__main__":
    N, M, R = map(int, IN().split())
    G = [[] for _ in range(N)]
    visited = [False for _ in range(N+1)]

    for _ in range(M):
        u, v = map(int, IN().split())

        heapq.heappush(G[u], v)
        heapq.heappush(G[v], u)

    def dfs(start):
        visited[start] = True
        print(start)

        for x in G[start]:
            if not visited[x]:
                dfs(x)

    dfs(R)
    print(0)