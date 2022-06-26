import sys
from collections import deque

IN = sys.stdin.readline

if __name__ == "__main__":
    N, M, K = map(int, IN().split())
    board = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[False for _ in range(M)] for _ in range(N)]
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for _ in range(K):
        n, m = map(int, IN().split())
        board[n-1][m-1] = 1

    def bfs(r, c):
        que = deque([(r, c)])
        count = 1

        while que:
            r, c = que.popleft()

            for mr, mc in move:
                dr, dc = r + mr, c + mc

                if 0 <= dr < N and 0 <= dc < M and board[dr][dc] == 1 and not visited[dr][dc]:
                    count += 1
                    visited[dr][dc] = True
                    que.append((dr, dc))

        return count

    result = 0
    for r in range(N):
        for c in range(M):
            if board[r][c] == 1 and not visited[r][c]:
                visited[r][c] = True
                result = max(result, bfs(r, c))

    print(result)