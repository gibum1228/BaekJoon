import copy
import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    R, C, N = map(int, IN().split())
    board = []
    move = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    position_boom, position_blank = [], []

    for r in range(R):
        arr = list(IN().rstrip())
        board.append(arr)
        for c in range(C):
            if arr[c] == ".":
                position_blank.append((r, c))
            else:
                position_boom.append((r, c))

    def bfs(N):
        global R, C, board, position_blank, position_boom
        sec, case = 1, 3 # 초기 1초는 아무것도 안 하니 1초부터 시작
        tmp_boom, tmp_blank = [], []

        while sec != N :
            print(sec + 1)
            if case == 3: # case 3: 빈 곳을 폭탄으로 채우기
                sec += 1
                case += 1

                for r, c in position_blank: # 빈 칸을 폭탄으로 변경
                    board[r][c] = "O"
                    tmp_boom.append((r, c))
                position_blank = []
            else: # case 4: 기존 폭탄이 터져서 주변이 빈 칸으로 됨
                sec += 1
                case = 3

                for r, c in position_boom:
                    if board[r][c] == "O":
                        board[r][c] = "."
                        tmp_blank.append((r, c))

                    for mr, mc in move:
                        dr, dc = r + mr, c + mc

                        if 0 <= dr < R and 0 <= dc < C and board[dr][dc] == "O":
                            board[dr][dc] = "."
                            tmp_blank.append((dr, dc))

                position_boom = copy.deepcopy(list(set(tmp_boom) - set(tmp_blank)))
                position_blank = copy.deepcopy(tmp_blank)
                tmp_boom, tmp_blank = [], []

    bfs(N)

    for result in board:
        print(*result, sep="")