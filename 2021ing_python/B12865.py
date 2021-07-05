def DP(N, K, objects):
    dp = [[0 for j in range(K+1)] for i in range (N+1)] # init

    # logic
    for i in range(1, N+1):
        for j in range(1, K+1):
            if objects[i-1][0] <= j: # 0부터 시작하기 때문에 i-1, 무게 한도를 넘지 않고 넣을 물건이 있다면
                # 새로운 물건을 넣었을 때와 기존 최적값을 비교해 큰 값을 선택
                dp[i][j] = max(objects[i-1][1] + dp[i-1][j - objects[i-1][0]], dp[i-1][j])
            else: # 새로운 물건을 넣을 수 없기 때문에 기존 최적값 선택
                dp[i][j] = dp[i-1][j]

    return dp[N][K]

if __name__ == "__main__":
    N, K = map(int, input().split())  # 물품 수, 무게 한도
    objects = []

    # input
    for i in range(N):
        objects.append([])

        W, V = map(int, input().split())

        objects[i].append(W)
        objects[i].append(V)

    print(DP(N, K, sorted(objects, key=lambda x : x[0])))