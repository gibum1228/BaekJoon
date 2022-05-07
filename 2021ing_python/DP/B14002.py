if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    dp = [0] * N
    arr = [[x] for x in A]

    # 1
    for i in range(N):
        for j in range(i):
            if A[i] > A[j] and dp[i] < dp[j]:
                arr[i] = arr[j] + [A[i]]
                dp[i] = dp[j]
        dp[i] += 1

    # 2
    max_count = max(dp)
    print(max_count)
    print(*arr[dp.index(max_count)])