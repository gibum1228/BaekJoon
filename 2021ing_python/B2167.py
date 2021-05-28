# 배열 크기 입력받기
n, m = map(int, input().split())
results = [list(map(int, input().split())) for _ in range(n)]
DP = [[0 for _ in range(m+1)] for _ in range(n+1)]

# DP 생성
for i in range(1, n+1):
    for j in range(1, m+1):
        DP[i][j] = results[i-1][j-1] + DP[i-1][j] + DP[i][j-1] - DP[i-1][j-1]

# 연산
for _ in range(int(input())):
    i, j, x, y = map(int, input().split())
    print(DP[x][y] - DP[x][j-1] - DP[i-1][y] + DP[i-1][j-1])