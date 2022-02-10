import sys

IN = sys.stdin.readline

def dfs(dept, x):
    global result

    if dept == 4:
        result = True
        return

    for i in graph[x]:
        if not visited[i]:
            visited[i] = True
            dfs(dept+1, i)
            visited[i] = False

if __name__ == "__main__":
    N, M = map(int, IN().split())
    graph = [[] for _ in range(N)]
    visited = [False for _ in range(N)]
    result = False

    for _ in range(M):
        a, b = map(int, IN().split())

        graph[a].append(b)
        graph[b].append(a)

    for i in range(N):
        visited[i] = True
        dfs(0, i)
        visited[i] = False
        if result: break

    print(1 if result else 0)