import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N = int(IN())
    arr = list(map(int, IN().split()))
    M = int(IN())
    start, end = 1, max(arr)

    while start <= end:
        mid = (start + end) // 2

        sum_num = 0
        for x in arr:
            sum_num += min(x, mid)

        if sum_num <= M:
            start = mid + 1
        else:
            end = mid - 1

    print(end)