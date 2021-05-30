K = int(input())
dp = [[] for _ in range(K + 1)]
dp[1] = [0, 1]

for i in range(2, K + 1):
    tmp = dp[i-1][0]
    dp[i].append(dp[i-1][1])
    dp[i].append(dp[i-1][1] + tmp)

print(dp[K][0], dp[K][1])