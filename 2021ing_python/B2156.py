import sys
sys.setrecursionlimit(10**6) # Recursion Runtime Error 방지 => 재귀 함수 깊이가 깊다면 발생

# dp
def logic(n):
    # 최대값이 정해져 있지 않다면
    if dp[n] is None:
        # 한 칸 건너 뛰고 더한 값과 연속으로 더한 값을 비교한 다음에, 기존 최대 누적값과 비교해 n에 삽입
        dp[n] = max(max(logic(n-2), logic(n-3) + wine[n-2]) + wine[n-1], logic(n-1))

    return dp[n]

if __name__ == "__main__":
    # input
    n = int(sys .stdin.readline())
    wine = [int(sys.stdin.readline()) for _ in range(n)]
    dp = [None for _ in range(n+1)]

    # init
    dp[0] = 0
    dp[1] = wine[0]
    '''
        n이 1이 아닐 경우,
        dp[2]의 최대값은 무조건 1 + 2이다.
    '''
    if n > 1:
        dp[2] = wine[0] + wine[1]

    # result
    print(logic(n))