import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, IN().split())
    graph = [[] for _ in range(N+1)]

    # input
    for _ in range(N-1):
        a, b, w = map(int, IN().split())

        graph[a].append((b, w))
        graph[b].append((a, w))

    def bfs(a, b):
        que = [(a, 0)]
        visited = [False] * (N+1)
        visited[a] = True

        while que:
            focus, cost = que.pop(0)

            for i, w in graph[focus]:
                if i == b:
                    print(cost + w)
                    return

                if not visited[i]:
                    que.append((i, cost + w))
                    visited[i] = True

    # bfs
    for _ in range(M):
        a, b = map(int, IN().split())

        bfs(a, b)