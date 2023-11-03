import sys
import copy

IN = sys.stdin.readline

if __name__ == "__main__":
    R, C, T = map(int, IN().split())
    board = []
    positions = set()
    ### input
    top_r, top_c, bottom_r, bottom_c = -1, 0, -1, 0
    for r in range(R):
        row = list(map(int, IN().split()))
        board.append(row)

        for c, x in enumerate(row):
            if x > 0:
                positions.add((r, c))
            if x == -1 and top_r == -1:
                top_r = r
    ### logic
    t = 0
    bottom_r = top_r + 1
    move = [(0, -1), (-1, 0), (0, 1), (1, 0)] # [0, 1, 2, 3] 좌 상 우 하
    while t < T:
        t += 1
        ## 미세먼지 확장할 거 탐색
        update = []
        for r, c in positions:
            minus_value = 0
            near_value = board[r][c] // 5

            for mr, mc in move:
                next_r, next_c = r + mr, c + mc

                if 0 <= next_r < R and 0 <= next_c < C \
                    and (next_r, next_c) not in [(top_r, top_c), (bottom_r, bottom_c)]:
                    minus_value += near_value
                    update.append((next_r, next_c, near_value))

            board[r][c] -= minus_value
        ## 미세먼지 확장한 거 업데이트
        for r, c, value in update:
            board[r][c] += value
            if (r, c) not in positions:
                positions.add((r, c))
        ## 공기청정기 작동
        # top
        r, c, head = top_r, 1, 2
        past = 0
        while not(top_r == r and top_c == c):
            tmp = board[r][c]
            board[r][c] = past
            past = tmp

            next_r, next_c = r + move[head][0], c + move[head][1]
            if next_r < 0:
                next_r = 0
                next_c -= 1
                head = 0
            if next_c < 0:
                next_c = 0
                next_r += 1
                head = 3
            if next_c >= C:
                next_c = C-1
                next_r -= 1
                head = 1

            r, c = next_r, next_c
        # bottom
        r, c, head = bottom_r, 1, 2
        past = 0
        while not (bottom_r == r and bottom_c == c):
            tmp = board[r][c]
            board[r][c] = past
            past = tmp

            next_r, next_c = r + move[head][0], c + move[head][1]
            if next_r >= R:
                next_r = R-1
                next_c -= 1
                head = 0
            if next_c < 0:
                next_c = 0
                next_r -= 1
                head = 1
            if next_c >= C:
                next_c = C - 1
                next_r += 1
                head = 3

            r, c = next_r, next_c
        ## position 탐색
        positions = set()
        for r in range(R):
            for c in range(C):
                if board[r][c] > 0:
                    positions.add((r, c))

    ### print
    result = 0
    for row in board:
        result += sum(row)
    print(result + 2)