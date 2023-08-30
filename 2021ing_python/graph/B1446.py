import sys
from collections import defaultdict

IN = sys.stdin.readline

if __name__ == "__main__":
    N, D = map(int, IN().split())
    dp = [10001 for _ in range(D+1)]
    dp[0] = 0
    info = defaultdict(list)

    for _ in range(N):
        start, end, distance = map(int, IN().split())
        info[end].append((start, distance))

    for idx in range(1, D+1):
        dp[idx] = dp[idx - 1] + 1

        for (start, distance) in info[idx]:
            dp[idx] = min(dp[idx], dp[start] + distance)

    print(dp[-1])