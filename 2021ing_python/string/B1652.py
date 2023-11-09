import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N = int(IN())
    board = [list(IN().rstrip()) for _ in range(N)]

    # init rows and cols
    rows, cols = [], [[] for _ in range(N)]
    for r in range(N):
        rows.append(board[r])

        for c in range(N):
            cols[c].append(board[r][c])

    # find 누울 자리
    row_count = 0
    for row in rows:
        count = 0

        for r in row:
            if r == '.':
                count += 1
            else:
                if count >= 2:
                    row_count += 1
                count = 0

        if count >= 2:
            row_count += 1

    col_count = 0
    for col in cols:
        count = 0

        for c in col:
            if c == '.':
                count += 1
            else:
                if count >= 2:
                    col_count += 1

                count = 0

        if count >= 2:
            col_count += 1

    print(row_count, col_count)