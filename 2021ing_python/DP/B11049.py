import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N = int(IN())
    dp = [[0 for _ in range(N)] for _ in range(N)]
    matrix = [list(map(int, IN().split())) for _ in range(N)]

    for i in range(1, N):
        for j in range(N - i):
            x = j + i
            dp[j][x] = 2 ** 32

            for k in range(j, x):
                dp[j][x] = min(dp[j][x], dp[j][k] + dp[k + 1][x] + matrix[j][0] * matrix[k][1] * matrix[x][1])

    print(dp[0][N - 1])