import sys
from collections import deque

IN = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, IN().split())
    board = [[0 for _ in range(N)] for _ in range(N)]
    r_position, c_position = map(int, IN().split())
    find_position = []
    # create find position
    for _ in range(M):
        A, B = map(int, IN().split())
        find_position.append((A, B))
    move = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

    def bfs(r, c, weight):
        que = deque([(r, c, weight)])

        while que:
            r, c, w = que.popleft()

            for mr, mc in move:
                dr, dc = mr + r, mc + c

                if 0 <= dr < N and 0 <= dc < N and board[dr][dc] == 0:
                    que.append((dr, dc, w + 1))
                    board[dr][dc] = w + 1

    bfs(r_position-1, c_position-1, 0)

    for a, b in find_position:
        print(board[a-1][b-1], end=" ")