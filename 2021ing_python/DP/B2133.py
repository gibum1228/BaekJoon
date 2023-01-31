import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N = int(IN())
    dp = [0 for _ in range(31)]
    dp[2] = 3

    for i in range(4, N+1):
        if i % 2 == 0:
            dp[i] = dp[i-2] * 3 + sum(dp[:i-2]) * 2 + 2

    print(dp[N])