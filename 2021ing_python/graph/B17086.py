import sys
from collections import deque

IN = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, IN().split())
    G = [list(map(int, IN().split())) for _ in range(N)]
    move = [
        [-1, -1], [-1, 0], [-1, 1],
        [0, -1], [0, 1],
        [1, -1], [1, 0], [1, 1]
    ]
    result = 0

    def bfs(start_r, start_c):
        global result
        que = deque([(start_r, start_c, 1)])
        visited = [[False for _ in range(M)] for _ in range(N)]
        visited[start_r][start_c] = True

        while que:
            r, c, count = que.popleft()

            for mr, mc in move:
                next_r = r + mr
                next_c = c + mc

                if 0 <= next_r < N and 0 <= next_c < M and not visited[next_r][next_c]:
                    if G[next_r][next_c] == 1:
                        result = max(result, count)
                        return

                    que.append((next_r, next_c, count + 1))
                    visited[next_r][next_c] = True

    for r in range(N):
        for c in range(M):
            if G[r][c] != 1:
                bfs(r, c)

    print(result)