import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    n, k = map(int, IN().split())
    c = []
    dp = [0 for i in range(k + 1)]

    for i in range(n):
        c.append(int(IN()))

    for i in range(1, k + 1):
        a = []
        for j in c:
            if j <= i and dp[i - j] != -1:
                a.append(dp[i - j])
        if not a:
            dp[i] = -1
        else:
            dp[i] = min(a) + 1

    print(dp[k])