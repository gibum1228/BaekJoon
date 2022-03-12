import sys
sys.setrecursionlimit(10**6)

IN = sys.stdin.readline

if __name__ == "__main__":
    N, M, S = map(int, IN().split())
    G = [[] for _ in range(N+1)]
    visited = [False for _ in range(N+1)]
    D = [-1 for _ in range(N+1)]
    T = [0 for _ in range(N+1)]

    for _ in range(M):
        u, v = map(int, IN().split())

        G[u].append(v)
        G[v].append(u)
    
    for arr in G:
        arr.sort(reverse=True)

    def dfs(start, count, T_count):
        D[start] = count
        T[start] = T_count
        visited[start] = True

        for x in G[start]:
            if not visited[x]:
                T_count = dfs(x, count+1, T_count+1)
        
        return T_count

    dfs(S, 0, 1)

    print(sum(list(map(lambda x, y: x*y, D, T))))