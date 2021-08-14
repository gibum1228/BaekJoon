import sys


def bfs():
    time = 0 # 소비 시간
    count = 0 # 마지막 치즈 갯수
    que = [(0, 0)] # 현재 포커싱 큐
    next_que = [] # 다음 포커싱 큐

    while que:
        time += 1 # 시간 증가
        count = len(que)

        # 녹일 치즈 좌표 구하기
        for i, j in que:
            if not visited[i][j] and board[i][j] == 0:
                visited[i][j] = True

                for di, dj in move:
                    dx = i + di
                    dy = j + dj

                    if 0 <= dx < w and 0 <= dy < h:
                        if board[dx][dy] == 0:
                            que.append((dx, dy))
                        else:
                            if not (dx, dy) in next_que:
                                next_que.append((dx, dy))
        # 치즈 녹이기
        for i, j in next_que:
            board[i][j] = 0

        # 녹은 치즈 좌표에서 너비 우선 탐색 수행하기
        que = next_que.copy()
        next_que = []
                        
    return time-1, count


if __name__ == '__main__':
    w, h = map(int, sys.stdin.readline().rstrip().split())
    board = []
    visited = [[False for _ in range(h)] for _ in range(w)] # 방문 여부
    move = [(0, -1), (1, 0), (0, 1), (-1, 0)] # 상우하좌

    for _ in range(w):
        board.append(list(map(int, sys.stdin.readline().rstrip().split())))

    time, count = bfs()

    print(time)
    print(count)