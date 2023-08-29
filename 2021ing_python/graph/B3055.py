import sys
from collections import deque

IN = sys.stdin.readline

if __name__ == "__main__":
    R, C = map(int, IN().split())
    move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    water_position = deque([])
    que = deque([])
    board = []

    for r in range(R):
        arr = list(IN().rstrip())

        for c, text in enumerate(arr):
            if text == '*':  # 물 위치 저장
                water_position.append((r, c))
            elif text == 'S':  # 출발 좌표
                que.append((r, c, 0))

        board.append(arr)

    while True:
        # 물 이동
        next_water_position = deque([])
        while water_position:
            r, c = water_position.popleft()

            for mr, mc in move:
                next_r = r + mr
                next_c = c + mc

                if 0 <= next_r < R and 0 <= next_c < C:
                    if board[next_r][next_c] == '.' or board[next_r][next_c] == 'S':
                        next_water_position.append((next_r, next_c))
                        board[next_r][next_c] = '*'
        water_position = next_water_position

        # 비버 이동
        next_que = deque([])
        while que:
            r, c, sec = que.popleft()

            for mr, mc in move:
                next_r = r + mr
                next_c = c + mc

                if 0 <= next_r < R and 0 <= next_c < C:
                    if board[next_r][next_c] == 'D':
                        print(sec + 1)
                        exit()

                    if board[next_r][next_c] == '.':
                        next_que.append((next_r, next_c, sec + 1))
                        board[next_r][next_c] = 'S'

        # trigger
        if next_que:
            que = next_que
        else:
            print("KAKTUS")
            break