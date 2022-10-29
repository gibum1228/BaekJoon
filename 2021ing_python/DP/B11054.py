import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    n = int(IN())
    arr = list(map(int, IN().rstrip().split()))
    dp_lis = [1] * n # 최장 증가 부분수열 - LIS
    dp_lds = [1] * n # 최장 감소 부분수열 - LDS

    # 합치기
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp_lis[i] = max(dp_lis[i], dp_lis[j] + 1)
            if arr[n-1-i] > arr[n-1-j]:
                dp_lds[n-1-i] = max(dp_lds[n-1-i], dp_lds[n-1-j] + 1)

    max_num = 0
    for i in range(n):
        max_num = max(max_num, dp_lis[i] + dp_lds[i])

    print(max_num - 1)