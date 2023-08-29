import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    for T in range(int(IN())):
        K = int(IN())
        arr = [0] + list(map(int, IN().split()))
        # S[i]는 1번부터 i번까지의 누적합
        S = [0 for _ in range(K + 1)]
        for i in range(1, K + 1):
            S[i] = S[i - 1] + arr[i]

        dp = [[0 for _ in range(K + 1)] for _ in range(K + 1)]
        for distance in range(2, K + 1): # 누적합 거리
            for start_idx in range(1, K + 2 - distance): # 시작점
                dp[start_idx][start_idx + distance - 1] = min([dp[start_idx][start_idx + i] + dp[start_idx + i + 1][start_idx + distance - 1] for i in range(distance - 1)]) + \
                                                            (S[start_idx + distance - 1] - S[start_idx - 1])

        print(dp[1][K])