import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    dp = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9] # 기본 수정
    for _ in range(int(IN())):
        N = int(IN())

        if N > len(dp):
            for i in range(len(dp), N):
                dp.append(dp[i-1] + dp[i-5]) # 가장 긴 변은 -1번째와 -5번째 삼각형을 합한 값임

        print(dp[N-1])