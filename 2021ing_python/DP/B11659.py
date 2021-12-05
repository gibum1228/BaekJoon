import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().split())
    original = list(map(int, input().rstrip().split()))
    dp = [0 for _ in range(N)]
    result = ""

    dp[0] = original[0]
    for i in range(1, N):
        dp[i] = dp[i-1] + original[i]

    for _ in range(M):
        start, end = map(int, input().split())

        if start == 1:
            result += str(dp[end-1]) + "\n"
        else:
            result += str(dp[end-1] - dp[start-2]) + "\n"

    print(result)