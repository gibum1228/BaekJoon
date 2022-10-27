import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    n = int(IN())
    dp = [1, 2, 3]

    for i in range(3, n):
        dp.append(dp[i-1] + dp[i-2])

    print(dp[n-1] % 10007)