import sys


if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().split())
    dp = [1, 1, 2]

    for i in range(3, N+1):
        dp.append(dp[i-1] * i)

    print((dp[N] // (dp[N-K] * dp[K])) % 10007)