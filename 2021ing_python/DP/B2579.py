import sys

input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    score = [0 for i in range(N)]
    dp = [0 for i in range(N)]

    # input
    for i in range(N):
        score[i] = int(input())

    dp[0] = score[0]
    if N > 2: dp[2] = max(score[0] + score[2], score[1] + score[2])
    if N > 1: dp[1] = score[0] + score[1]

    # DP
    for i in range(3, N):
        dp[i] = max(dp[i-3]+score[i-1]+score[i], dp[i-2]+score[i])

    print(dp[N-1])