import sys
from collections import deque

IN = sys.stdin.readline

if __name__ == "__main__":
    R, C = 12, 6
    board = [list(IN().rstrip()) for _ in range(R)]
    move= [[-1, 0], [1, 0], [0, 1], [0, -1]]
    # print("원본 >>")
    # print(*board, sep='\n')

    sec = 0
    while True:
        visited = [[False for _ in range(C)] for _ in range(R)]

        ### 4개 이상 찾기
        for r in range(R):
            for c in range(C):
                if not visited[r][c] and board[r][c] != '.':
                    key = board[r][c]
                    visited[r][c] = True
                    que = deque([[r, c]])
                    positions = []

                    while que:
                        now_r, now_c = que.popleft()
                        positions.append([now_r, now_c])

                        for mr, mc in move:
                            next_r, next_c = now_r + mr, now_c + mc

                            if (0 <= next_r < R and 0 <= next_c < C and
                                    board[next_r][next_c] == key and
                                    not visited[next_r][next_c]):
                                visited[next_r][next_c] = True
                                que.append([next_r, next_c])

                    if len(positions) >= 4:
                        for now_r, now_c in positions:
                            board[now_r][now_c] = '_'
        ### 연쇄 여부 판단 후 범위 구하기 or 게임 종료
        trigger = True
        for row in board:
            if '_' in row:
                sec += 1
                trigger = False
                break
        if trigger: break # 연쇄 반응이 없었다면 게임 종료

        ### 뿌요뿌요 내리기
        for c in range(C):
            stack = []
            # stack 채우기
            for r in range(R-1, -1, -1):
                if board[r][c] not in ['_', '.']:
                    stack.append(board[r][c])
            while len(stack) < R:
                stack.append('.')
            # 변환
            for r in range(R-1, -1, -1):
                board[r][c] = stack[R-r-1]
        # print(sec, "연쇄 후")
        # print(*board, sep='\n')

    print(sec)