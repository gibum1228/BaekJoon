import sys
from collections import deque

IN = sys.stdin.readline


def change_head(now_head, next_order):
    db = {'top': 1, 'right': 2, 'down': 3, 'left': 4,
          1: 'top', 2: 'right', 3: 'down', 4: 'left'}

    order = db[now_head]

    if next_order == 'L':  # 왼쪽으로 90도 회전
        order -= 1
        if order == 0: order = 4
    else:  # 오른쪽으로 90도 회전
        order += 1
        if order == 5: order = 1

    return db[order]


if __name__ == "__main__":
    N = int(IN())  # (N, N) 보드
    board = [[0 for _ in range(N)] for _ in range(N)]  # 0 빈공간
    orders = deque()
    now_r, now_c = 0, 0
    now_head = 'right'
    snake = deque([(0, 0)])
    sec = 0

    for _ in range(int(IN())):  # 사과 위치
        r, c = map(int, IN().split())
        board[r - 1][c - 1] = 1  # 1 사과

    for _ in range(int(IN())):  # 방향 변환 횟수
        x, c = IN().split()

        orders.append((int(x), c))

    next_sec, next_order = orders.popleft()
    while True:
        sec += 1
        # 머리 방향에 따라 전진
        if now_head == 'right':
            now_c += 1
        elif now_head == 'left':
            now_c -= 1
        elif now_head == 'top':
            now_r -= 1
        elif now_head == 'down':
            now_r += 1

        if 0 <= now_r < N and 0 <= now_c < N:
            if (now_r, now_c) in snake:  # 몸통에 충돌
                break
            else:
                snake.append((now_r, now_c))  # 머리 추가하기

                if board[now_r][now_c] == 1:  # 사과면 꼬리 이동할 필요 없음
                    board[now_r][now_c] = 0
                else:  # 꼬리 이동
                    snake.popleft()

        else:  # 벽에 충돌
            break

        if sec == next_sec:
            now_head = change_head(now_head, next_order)
            next_sec, next_order = orders.popleft() if orders else (0, 0)

    print(sec)