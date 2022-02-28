import sys
import heapq
sys.setrecursionlimit(10**6)

IN = sys.stdin.readline

if __name__ == "__main__":
    N, M, R = map(int, IN().split())
    G = [[] for _ in range(N+1)]
    visited = [False for _ in range(N+1)]
    results = [0 for _ in range(N+1)]

    for _ in range(M):
        u, v = map(int, IN().split())

        heapq.heappush(G[u], v)
        heapq.heappush(G[v], u)

    def dfs(start, count):
        results[start] = count
        visited[start] = True

        for x in G[start]:
            if not visited[x]:
                count = dfs(x, count+1)

        return count

    dfs(R, 1)

    print("\n".join(map(str, results[1:])))