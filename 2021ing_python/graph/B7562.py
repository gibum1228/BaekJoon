import sys
import copy
from collections import deque

IN = sys.stdin.readline

if __name__ == "__main__":
    T = int(IN())

    for _ in range(T):
        I = int(IN())
        now_row, now_col = map(int, IN().split())
        move_row, move_col = map(int, IN().split())
        board = [[0 for _ in range(I)] for _ in range(I)]
        move = [(-1, -2), (-2, -1), (-1, 2), (-2, 1), (1, -2), (2, -1), (2, 1), (1, 2)]


        if now_row == move_row and now_col == move_col:
            print(0)
        else:
            que = deque([(now_row, now_col, 0)])

            while que:
                row, col, cnt = que.popleft()

                for d_r, d_c in move:
                    n_r, n_c = row + d_r, col + d_c

                    if 0 <= n_r < I and 0 <= n_c < I and board[n_r][n_c] == 0:
                        board[n_r][n_c] = cnt + 1
                        if n_r == move_row and n_c == move_col:
                            que = []
                            break
                        que.append((n_r, n_c, cnt + 1))

            print(board[move_row][move_col])