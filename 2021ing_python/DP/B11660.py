import sys


input = sys.stdin.readline


if __name__ == "__main__":
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0 for _ in range(N+1)] for _ in range(N+1)]

    # dp
    for i in range(1, N+1):
        for j in range(1, N+1):
            dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + board[i-1][j-1]

    # order
    for i in range(M):
        x1, y1, x2, y2 = map(int, input().split())

        print(dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1])