import copy
import sys
from collections import deque

IN = sys.stdin.readline

if __name__ == "__main__":
    N, M, D = map(int, IN().split())
    board = deque([list(map(int, IN().split())) for _ in range(N)])
    move = [(0, -1), (-1, 0), (0, 1)] # 거리 가까운 왼쪽 거부터 제거

    result = 0
    for archer1 in range(M - 2):
        for archer2 in range(archer1 + 1, M - 1):
            for archer3 in range(archer2 + 1, M):
                # print("="*20)
                # print("궁수 배치도 >>", archer1, archer2, archer3)

                die = 0
                copy_board = copy.deepcopy(board)
                while copy_board:
                    del_enemy_positions = set()

                    ### 궁수별 제거할 적 위치 찾기
                    for archer in [archer1, archer2, archer3]: # 궁수 한 명씩 하나 제거하기
                        que = deque([(len(copy_board) - 1, archer, 1)])
                        visited = {(len(copy_board) - 1, archer)}

                        while que: # bfs
                            r, c, d = que.popleft()

                            if copy_board[r][c] == 1:
                                if (r, c) not in del_enemy_positions:
                                    die += 1
                                    del_enemy_positions.add((r, c))
                                break

                            for mr, mc in move:
                                next_r, next_c = r + mr, c + mc

                                if (next_r >= 0 and 0 <= next_c < M
                                        and (next_r, next_c) not in visited
                                        and d+1 <= D):
                                    que.append((next_r, next_c, d+1))
                                    visited.add((next_r, next_c))
                    ### 맵에서 적 삭제
                    for r, c, in del_enemy_positions:
                        copy_board[r][c] = 0
                    # print(N - len(copy_board), "턴 결과 >>", "제거 수 ==", die)
                    # print(*copy_board, sep='\n')
                    ### 아래로 전진
                    copy_board.pop()

                # 최대 적 제거 수 업데이트
                result = max(result, die)

    print(result)