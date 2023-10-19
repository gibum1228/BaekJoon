import sys
from collections import deque

IN = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, IN().split())

    # find cheese
    cheese_positions = set()
    board = []
    for r in range(N):
        row = list(map(int, IN().split()))
        board.append(row)

        for c, x in enumerate(row):
            if x == 1:
                cheese_positions.add((r, c))

    # find boundary
    boundary_positions = set()
    move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited = [[False for _ in range(M)] for _ in range(N)]
    visited[0][0] = True
    que = deque([(0, 0)])

    while que:
        r, c = que.popleft()

        for mr, mc in move:
            next_r, next_c = r + mr, c + mc

            if 0 <= next_r < N and 0 <= next_c < M:
                if board[next_r][next_c] == 0 and not visited[next_r][next_c]:
                    visited[next_r][next_c] = True
                    que.append((next_r, next_c))
                elif board[next_r][next_c] == 1:
                    boundary_positions.add((r, c))
    # print("원본")
    # print(*board, sep='\n')
    # 초 세기
    sec = 0
    while cheese_positions:
        sec += 1
        del_cheese_positions = set() # 치즈 삭제 == 경계 추가

        # 치즈 삭제
        for c_r, c_c in cheese_positions:
            count = 0

            for mr, mc in move:
                next_r, next_c = c_r + mr, c_c + mc

                if (0 <= next_r < N and 0 <= next_c < M and
                        board[next_r][next_c] == 0 and
                        (next_r, next_c) in boundary_positions):
                    count += 1

            if count >= 2:
                board[c_r][c_c] = 0
                del_cheese_positions.add((c_r, c_c))

        # 치즈 안에 있는 빈 공간 정보 추가하기
        que = deque(del_cheese_positions)
        while que:
            r, c = que.popleft()

            for mr, mc in move:
                next_r, next_c = r + mr, c + mc

                if (0 <= next_r < N and 0 <= next_c < M and
                        (next_r, next_c) not in boundary_positions and
                        (next_r, next_c) not in del_cheese_positions and
                        board[next_r][next_c] == 0):
                    del_cheese_positions.add((next_r, next_c))
                    que.append((next_r, next_c))

        # update
        cheese_positions -= del_cheese_positions
        boundary_positions = boundary_positions | del_cheese_positions

        # for r, c in cheese_positions:
        #     board[r][c] = 9
        # for r, c in boundary_positions:
        #     board[r][c] = 5
        # for r, c in del_cheese_positions:
        #     board[r][c] = 3

        # print(sec, "초 후")
        # print(*board, sep='\n')

    print(sec)