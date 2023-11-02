import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, IN().split())
    height = list(map(int, IN().split()))
    start, end = 1, max(height)

    while start <= end:
        mid = (start + end) // 2

        sum_num = 0
        for x in height:
            if x >= mid:
                sum_num += (x - mid)

        if sum_num >= M:
            start = mid + 1
        else:
            end = mid - 1

    print(end)