import sys
from collections import deque

IN = sys.stdin.readline

if __name__ == "__main__":
    N = int(IN())
    G = [list(map(int, IN().rstrip().split())) for _ in range(N)]
    results = [[0 for _ in range(N)] for _ in range(N)]
    result = ""
    
    def bfs(i, j):
        que = deque([(i, j)])
        visited = [False for _ in range(N)]
        visited[j] = True

        while que:
            _, w = que.popleft()
            results[i][w] = 1

            for x in range(N):
                if G[w][x] == 1 and not visited[x]:
                    que.append((w, x))
                    visited[x] = True
    
    for i in range(N):
        for j in range(N):
            if G[i][j] == 1:
                bfs(i, j)

    for s in results:
        result += " ".join(map(str, s)) + "\n"
    
    print(result)