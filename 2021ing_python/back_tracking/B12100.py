import sys
from copy import deepcopy

IN = sys.stdin.readline

if __name__ == "__main__":
    N = int(IN())
    board = [list(map(int, IN().rstrip().split())) for _ in range(N)]
    answer = 0


    def moving(board, cmd):
        if cmd == 0:  # right
            for r in range(N):
                pointer = N - 1

                for c in range(N - 2, -1, -1):
                    if board[r][c]:
                        tmp = board[r][c]
                        board[r][c] = 0

                        if board[r][pointer] == 0:
                            board[r][pointer] = tmp
                        elif board[r][pointer] == tmp:
                            board[r][pointer] = tmp * 2
                            pointer -= 1
                        else:
                            pointer -= 1
                            board[r][pointer] = tmp
        elif cmd == 1:  # down
            for r in range(N):
                pointer = N - 1

                for c in range(N - 2, -1, -1):
                    if board[r][c]:
                        tmp = board[r][c]
                        board[r][c] = 0

                        if board[pointer][c] == 0:
                            board[pointer][c] = tmp
                        elif board[pointer][c] == tmp:
                            board[pointer][c] = tmp * 2
                            pointer -= 1
                        else:
                            pointer -= 1
                            board[pointer][c] = tmp
        elif cmd == 2:  # left
            for r in range(N):
                pointer = 0

                for c in range(1, N):
                    if board[r][c]:
                        tmp = board[r][c]
                        board[r][c] = 0

                        if board[r][pointer] == 0:
                            board[r][pointer] = tmp
                        elif board[r][pointer] == tmp:
                            board[r][pointer] = tmp * 2
                            pointer += 1
                        else:
                            pointer += 1
                            board[r][pointer] = tmp
        else:  # up
            for r in range(N):
                pointer = 0

                for c in range(1, N):
                    if board[r][c]:
                        tmp = board[r][c]
                        board[r][c] = 0

                        if board[pointer][c] == 0:
                            board[pointer][c] = tmp
                        elif board[pointer][c] == tmp:
                            board[pointer][c] = tmp * 2
                            pointer += 1
                        else:
                            pointer += 1
                            board[pointer][c] = tmp

        return board


    def dfs(board, cnt):
        global answer

        # 최대 5번을 움직였기 때문에 종료
        if cnt == 5:
            answer = max(answer, max(map(max, board)))
            return

        for i in range(4):
            tmp_board = moving(deepcopy(board), i)
            dfs(tmp_board, cnt + 1)


    dfs(board, 0)
    print(answer)