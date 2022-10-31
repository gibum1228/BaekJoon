import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    n = int(IN())
    arr = list(map(int, IN().rstrip().split()))
    dp = [arr[0]]

    for i in range(1, n):
        dp.append(max(arr[i], arr[i] + dp[i-1]))

    print(max(dp))