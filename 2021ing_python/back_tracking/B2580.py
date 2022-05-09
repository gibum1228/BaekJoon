import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    board = [list(map(int, IN().rstrip().split())) for _ in range(9)]
    zero_position = [(i, j) for i in range(9) for j in range(9) if not board[i][j]]
    num = [i for i in range(1, 10)]

    def bt(n):
        global board

        if n == len(zero_position):
            for i in board:
                print(*i)
            exit()

        row, col = zero_position[n]
        a, b = row // 3, col // 3
        candidate = num[:]

        for i in range(a * 3, (a + 1) * 3):
            for j in range(b * 3, (b + 1) * 3):
                if board[i][j] in candidate:
                    candidate.remove(board[i][j])

        for i in range(9):
            if board[row][i] in candidate:
                candidate.remove(board[row][i])
            if board[i][col] in candidate:
                candidate.remove(board[i][col])

        for i in candidate:
            board[row][col] = i
            bt(n + 1)
            board[row][col] = 0

    bt(0)