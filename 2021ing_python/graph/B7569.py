import sys
from collections import deque

IN = sys.stdin.readline

if __name__ == "__main__":
    C, R, H = map(int, IN().split())
    move = [(0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1), (1, 0, 0), (-1, 0, 0)]
    board = []
    position, zero_position = deque(), deque()

    # input board
    for h in range(H):
        board.append([])
        for r in range(R):
            board[h].append(list(map(int, IN().rstrip().split())))

            for c in range(C):
                if board[h][r][c] == 1:
                    position.append((h, r, c))
                elif board[h][r][c] == 0:
                    zero_position.append((h, r, c))

    # search
    def bfs(position):
        while position:
            h, r, c = position.popleft()

            for mh, mr, mc in move:
                dh, dr, dc = h + mh, r + mr, c + mc

                if 0 <= dh < H and 0 <= dr < R and 0 <= dc < C and board[dh][dr][dc] == 0:
                    board[dh][dr][dc] = board[h][r][c] + 1
                    position.append((dh, dr, dc))

    bfs(position)
    # result
    day = -1 if zero_position else 0
    for h, r, c in zero_position:
        if board[h][r][c] == 0:
            day = -1
            break
        else:
            day = max(day, board[h][r][c] - 1)

    print(day)