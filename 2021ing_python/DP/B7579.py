import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, IN().split()) # 현재 실행중인 앱, 새로운 앱을 실행시키기 위해 필요한 메모리
    A = [0] + list(map(int, IN().split())) # 현재 실행중인 앱이 사용중인 메모리
    c = [0] + list(map(int, IN().split())) # 비활성화 했을 때 필요한 비용 -> 최소화시켜서 M을 차지해라
    dp = [[0 for _ in range(sum(c) + 1)] for _ in range(N+1)]
    min_memory = sum(c)

    for i in range(1, N+1): # 하나의 앱에 대한 최적해 구하기
        app = A[i] # 사용중인 앱의 메모리
        cost = c[i] # 앱을 비활성화 했을 때 사용되는 비용

        for j in range(1, sum(c) + 1): # 해당 앱을 기준으로 cost별 최적해 업데이트하기
            if j < cost: # 현재 앱으로 비용 j에 대한 업데이트 못 함
                dp[i][j] = dp[i-1][j] # 기존 최적해로 채우기
            else:
                dp[i][j] = max(dp[i-1][j], app + dp[i-1][j-cost]) # 기존 최적해 vs 현재 가능한 조합(현재 값 + 현재 상황을 제외했을 때 최적해)

            if dp[i][j] >= M:
                min_memory = min(min_memory, j) # 최소 cost 업데이트

    print(min_memory if M != 0 else 0)