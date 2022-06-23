import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N = int(IN())
    info = [list(map(int, IN().rstrip().split())) for _ in range(N)]
    dp = [0] * (N + 1)

    for i in range(N-1, -1, -1):
        T, P = info[i]

        if i + T > N:
            dp[i] = dp[i+1]
        else:
            dp[i] = max(dp[i+1], P + dp[i + T])

    print(max(dp))