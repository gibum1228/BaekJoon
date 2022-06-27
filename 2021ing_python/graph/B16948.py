import sys
from collections import deque

IN = sys.stdin.readline

if __name__ == "__main__":
    N = int(IN())
    r1, c1, r2, c2 = map(int, IN().split())
    board = [[-1 for _ in range(N)] for _ in range(N)]
    move = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]

    def bfs(r, c):
        que = deque([(r, c)])
        board[r][c] = 0

        while que:
            r, c = que.popleft()

            for mr, mc in move:
                dr, dc = r + mr, c + mc

                if 0 <= dr < N and 0 <= dc < N and board[dr][dc] == -1:
                    board[dr][dc] = board[r][c] + 1
                    que.append((dr, dc))
                    if dr == r2 and dc == c2:
                        return

    bfs(r1, c1)

    print(board[r2][c2])