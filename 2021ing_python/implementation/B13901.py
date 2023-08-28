import sys
from collections import deque

IN = sys.stdin.readline

if __name__ == "__main__":
    # 맵 크기
    R, C = map(int, IN().split())
    board = [[0 for _ in range(C)] for _ in range(R)]
    # 장애물 개수 및 위치
    k = int(IN())
    for _ in range(k):
        br, bc = map(int, IN().split())
        board[br][bc] = -1
    # 시작 위치
    sr, sc = map(int, IN().split())
    board[sr][sc] = 1
    # 상하좌우 순서
    role = deque(list(map(int, IN().split()))) # 1은 위, 2는 아래, 3은 왼쪽, 4는 오른쪽
    move = {
        1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)
    }

    count = 0
    while True:
        if count == 4:
            print(sr, sc)
            break

        order = role[0]
        next_sr = sr + move[order][0]
        next_sc = sc + move[order][1]

        if 0 <= next_sr < R and 0 <= next_sc < C and board[next_sr][next_sc] == 0:
            sr, sc = next_sr, next_sc
            board[sr][sc] = 1
            count = 0
        else:
            role.append(role.popleft())
            count += 1