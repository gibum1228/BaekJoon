import sys
import copy

IN = sys.stdin.readline

if __name__ == "__main__":
    N = int(IN())
    P = [0] + list(map(int, IN().rstrip().split()))
    dp = copy.deepcopy(P)

    for i in range(2, N+1):
        for j in range(1, i):
            if dp[i] < dp[i-j] + dp[j]:
                dp[i] = dp[i-j] + dp[j]
    
    print(dp[N])