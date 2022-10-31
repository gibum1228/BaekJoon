import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N = int(IN())
    dp = [1, 1, 2, 3, 5, 8]

    for i in range(len(dp), N):
        dp.append(dp[i-1] + dp[i-2])

    print(dp[N-1])