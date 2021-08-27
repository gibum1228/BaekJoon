import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    triangle = []

    # input
    for i in range(n):
        triangle.append(list(map(int, sys.stdin.readline().split())))

    # logic
    for i in range(1, n+1):
        for j in range(1, i+1):
            if j == 1: # 맨 왼쪽 케이스
                dp[i][j] = dp[i-1][j] + triangle[i-1][j-1]
            elif i == j: # 맨 오른쪽 케이스
                dp[i][j] = dp[i-1][j-1] + triangle[i-1][j-1]
            else: # 중간에 있는 케이스
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i-1][j-1]

    print(max(dp[n]))