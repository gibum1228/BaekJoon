import sys
from collections import deque

IN = sys.stdin.readline

if __name__ == "__main__":
    R, C = map(int, IN().split())
    board = [list(map(int, IN().rstrip().split())) for _ in range(R)]
    move = [(-1, 0), (1, 0), (0, -1), (0, 1),
            (-1, -1), (-1, 1), (1, -1), (1, 1)]
    count = 0

    def bfs(r, c):
        que = deque([(r, c)])

        while que:
            r, c = que.popleft()

            for mr, mc in move:
                dr, dc = r + mr, c + mc

                if 0 <= dr < R and 0 <= dc < C and board[dr][dc] == 1:
                    board[dr][dc] = 2
                    que.append((dr, dc))

    for r in range(R):
        for c in range(C):
            if board[r][c] == 1:
                bfs(r, c)
                count += 1

    print(count)