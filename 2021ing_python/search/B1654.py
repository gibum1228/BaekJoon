import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    K, N = map(int, IN().split())
    lan_line = [int(IN()) for _ in range(K)]
    start, end = 1, max(lan_line)

    while start <= end:
        mid = (start + end) // 2

        sum_count = 0
        for x in lan_line:
            sum_count += x // mid

        if sum_count >= N:
            start = mid + 1
        else:
            end = mid - 1

    print(end)