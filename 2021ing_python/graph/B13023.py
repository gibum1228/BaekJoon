import sys

IN = sys.stdin.readline

def dfs(x):
    visited[x] = True

    for next_x in graph[x]:
        if not visited[next_x]:
            dfs(next_x)


if __name__ == "__main__":
    N, M = map(int, IN().split())
    graph = [[] for _ in range(N)]
    visited = [False for _ in range(N)]
    start = -1

    for _ in range(M):
        a, b = map(int, IN().split())

        graph[a].append(b)
        graph[b].append(a)

        if start == -1: start = a

    dfs(start)

    print(1 if visited.count(False) == 0 else 0)