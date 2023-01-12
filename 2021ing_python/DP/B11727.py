import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    n = int(IN())
    dp = [-1, 1, 3, 5, 11, 21] # 21+22=43, 43+42=85, 85+86 = 171

    for i in range(6, n+1):
        dp.append(dp[i-1] + dp[i-2]*2)

    print(dp[n] % 10007)