import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, IN().split())
    A = list(map(int, IN().split()))
    results = [0] * M
    sum_num = 0

    for i in range(N):
        sum_num += A[i]
        results[sum_num % M] += 1

    result = results[0]
    for num in results:
        result += num * (num - 1) // 2

    print(result)