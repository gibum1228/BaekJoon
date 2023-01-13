import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, IN().split())
    G = {k: [] for k in range(1, N+1)}
    for _ in range(M):
        A, B = map(int, IN().split())
        G[B].append(A)
    X = int(IN())
    visited = [False] * (N+1)

    def dfs(start):
        que = [start]
        visited[start] = True
        result = 0

        while que:
            now_node = que.pop()

            for next_node in G[now_node]:
                if not visited[next_node]:
                    que.append(next_node)
                    visited[next_node] = True
                    result += 1

        return result

    print(dfs(X))