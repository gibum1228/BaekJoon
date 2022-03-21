import sys
sys.setrecursionlimit(10**6)

IN = sys.stdin.readline

if __name__ == "__main__":
    N, M, S = map(int, IN().split())
    G = [[] for _ in range(N+1)]
    visited = [False for _ in range(N+1)]
    R = [-1 for _ in range(N+1)]

    for _ in range(M):
        u, v = map(int, IN().split())

        G[u].append(v)
        G[v].append(u)
    
    for arr in G:
        arr.sort(reverse=True)

    def dfs(start, count):
        R[start] = count
        visited[start] = True

        for x in G[start]:
            if not visited[x]:
                dfs(x, count+1)

    dfs(S, 0)

    print("\n".join(map(str, R[1:])))