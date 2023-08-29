import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    R, C = map(int, IN().split())
    board = [list(IN().rstrip()) for _ in range(R)]
    move = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    # logic
    change_positions = []
    min_r, min_c = 11, 11
    max_r, max_c = -1, -1
    for r in range(R):
        for c in range(C):
            if board[r][c] == 'X':
                count = 0

                for mr, mc in move:
                    next_r = r + mr
                    next_c = c + mc

                    if 0 <= next_r < R and 0 <= next_c < C:
                        if board[next_r][next_c] == '.':
                            count += 1
                    else:
                        count += 1

                if count >= 3:
                    change_positions.append((r, c))
                else:
                    min_r = min(min_r, r)
                    min_c = min(min_c, c)
                    max_r = max(max_r, r)
                    max_c = max(max_c, c)

    for r, c in change_positions:
        board[r][c] = '.'

    # print
    for row in board[min_r:max_r+1]:
        print(''.join(row[min_c:max_c+1]))