import sys


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    board = []
    count = 0 # 청소한 칸

    r, c, d = map(int, sys.stdin.readline().split()) # (r, c), d = [0: 북, 1: 동, 2: 남, 3: 서]
    for i in range(N):
        board.append(list(map(int, sys.stdin.readline().rstrip().split())))

    while True:
        # 1
        if board[r][c] == 0:
            board[r][c] = -1
            count += 1

        # 2-c, 2-d
        if board[r-1][c] != 0 and board[r+1][c] != 0 and board[r][c-1] != 0 and board[r][c+1] != 0:
            if d == 0:
                if board[r+1][c] == 1:
                    break
                else:
                    r += 1
            elif d == 1:
                if board[r][c-1] == 1:
                    break
                else:
                    c -= 1
            elif d == 2:
                if board[r-1][c] == 1:
                    break
                else:
                    r -= 1
            elif d == 3:
                if board[r][c+1] == 1:
                    break
                else:
                    c += 1

            continue

        # 2-a, 2-b
        if d == 0:
            if board[r][c-1] == 0:
                c -= 1
            d = 3
        elif d == 1:
            if board[r-1][c] == 0:
                r -= 1
            d = 0
        elif d == 2:
            if board[r][c+1] == 0:
                c += 1
            d = 1
        elif d == 3:
            if board[r+1][c] == 0:
                r += 1
            d = 2

    print(count)