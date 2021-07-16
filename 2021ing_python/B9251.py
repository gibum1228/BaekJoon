import sys

if __name__ == '__main__':
    standard_str = input()
    compared_str = input()

    dp = [[0 for _ in range(len(standard_str)+1)] for _ in range(len(compared_str)+1)]

    # computing
    for i in range(1, len(compared_str)+1):
        for j in range(1, len(standard_str)+1):
            # 수열에 현재 단어를 추가 할 수 있으면
            if compared_str[i-1] == standard_str[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1 # 전 단계 수열 최대 길이에서 + 1
            else:
                # 전 단계 기준 최고값([i-1][j])과 현재 포커싱 중인 단어 기준 최고값([i][j-1] 중 최고값 선별
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    print(dp[len(compared_str)][len(standard_str)])