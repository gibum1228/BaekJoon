import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N = int(IN())
    arr = list(map(int, IN().split()))
    dp = [[True for _ in range(N)] for _ in range(N)]

    # dp - 기본값이 전부 True니깐 팰린드롬이 아닌 것만 찾으면 됨
    for bias in range(N):
        for start in range(N-bias):
            end = start + bias

            if arr[start] != arr[end]: # 양 끝이 다르면 팰린드롬 아님
                dp[start][end] = False
            elif arr[start] == arr[end] and end-start >= 2: # 양 끝이 같으면 start+1, end-1만 보면 됨
                if not dp[start+1][end-1]:
                    dp[start][end] = False

    # M개 만큼 S, E 입력 받기
    for _ in range(int(IN())):
        S, E = map(int, IN().split())

        print(1 if dp[S-1][E-1] else 0)