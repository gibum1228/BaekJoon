import sys

def dfs(i, j):
    global trigger
    visited[i][j] = True

    for m in range(len(move)):
        x = i + move[m][0] # 주변 산봉우리 확인
        y = j + move[m][1]

        if (0 <= x < N) and (0 <= y < M):
            if farm[i][j] < farm[x][y]: # 자기보다 높은 산봉우리가 있다면
                trigger = False # farm[i][j]는 산봉우리가 아님
            if not visited[x][y] and farm[x][y] == farm[i][j]: # 같은 높이의 산봉우리 확인
                dfs(x, y)

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    farm = [[] for _ in range(N)]
    visited = [[False for _ in range(M)] for _ in range(N)]
    move = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)] # 12시부터 시계 방향
    count = 0

    # create farm
    for i in range(N):
        farm[i] = list(map(int, sys.stdin.readline().split()))

    # logic
    for i in range(N):
        for j in range(M):
            if farm[i][j] > 0 and not visited[i][j]:
                trigger = True # init
                dfs(i, j)
                if trigger: # farm[i][j]는 산봉우리임
                    count += 1

    print(count)