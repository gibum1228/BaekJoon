import sys
import copy


def bfs():
    global result, virus_position
    count = 0 # 현재 경우의 빈 칸 개수
    que = virus_position.copy()
    copy_arr = copy.deepcopy(arr)
    
    # 바이러스 BFS 전파
    while que:
        x, y = que.pop(0) # 바이러스 위치 받아오기

        for i, j in move:
            dx = x + i
            dy = y + j
            
            if 0 <= dx < N and 0 <= dy < M: # 주위에
                if copy_arr[dx][dy] == 0: # 빈 칸이 있다면
                    copy_arr[dx][dy] = 2 # 바이러스 전파
                    que.append((dx, dy))

    # 빈 칸 세기
    for i in range(N):
        count += copy_arr[i].count(0)
    
    # 값 비교
    result = max(result, count)

def create_wall(count, x):
    if count == 3: # 벽 다 세웠으니 바이러스 전파
        bfs()
        return

    # 벽 세우기
    for i in range(x, N):
        for j in range(M):
            if arr[i][j] == 0:
                arr[i][j] = 1
                create_wall(count+1, i)
                arr[i][j] = 0


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    board = []
    virus_position = []
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우
    result = 0 # 안전 영역의 최대 크기

    # input
    for i in range(N):
        board.append(list(map(int, sys.stdin.readline().rstrip().split())))

        # 바이러스 좌표값 기억
        for j in range(M):
            if board[i][j] == 2:
                virus_position.append((i, j))

    for i in range(N):
        for j in range(M):
            # 벽 세우기
            if board[i][j] == 0:
                arr = copy.deepcopy(board)
                
                arr[i][j] = 1
                create_wall(1, i)
                arr[i][j] = 0

    print(result)