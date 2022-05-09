import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    board = [list(map(int, list(IN().rstrip()))) for _ in range(9)]
    zero_position = [(i, j) for i in range(9) for j in range(9) if not board[i][j]]
    num = [i for i in range(1, 10)]

    def back_tracking(n):
        global board

        if n == len(zero_position):
            for i in board:
                print(*i, sep="")
            exit()

        row, col = zero_position[n]
        a, b = row // 3, col // 3
        cand = num[:]

        # 박스 내 채워진 숫자 제거
        for i in range(a * 3, (a + 1) * 3):
            for j in range(b * 3, (b + 1) * 3):
                if board[i][j] in cand:
                    cand.remove(board[i][j])

        # 가로 세로 내 채워진 숫자 제거
        for i in range(9):
            if board[row][i] in cand:
                cand.remove(board[row][i])
            if board[i][col] in cand:
                cand.remove(board[i][col])

        for i in cand:
            board[row][col] = i
            back_tracking(n + 1)
        board[row][col] = 0

    back_tracking(0)