import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(start):
    visited[start] = True

    for i in graph[start]:
        if not visited[i]:
            dfs(i)

if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    visited = [False for _ in range(N+1)]
    count = 0

    for _ in range(M):
        u, v = map(int, input().split())

        graph[u].append(v)
        graph[v].append(u)

    for i in range(1, N+1):
        if not visited[i]:
            count += 1
            dfs(i)

    print(count)