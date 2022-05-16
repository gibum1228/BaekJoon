import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    n, k = map(int, IN().split())
    weight = [int(IN()) for _ in range(n)]
    dp = [0] * (k + 1)
    dp[0] = 1

    for i in weight:
        for j in range(i, k + 1):
            if j - i >= 0:
                dp[j] += dp[j - i]

    print(dp[k])