import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N, K = map(int, IN().split())
    A = list(map(int, IN().rstrip().split()))
    count = 0
    results = -1

    end = N - 1
    while end > 0:
        swap_point = 0

        for i in range(end):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                swap_point = i
                count += 1

                if count == K:
                    results = f"{A[i]} {A[i + 1]}"

        end = swap_point

    print(results)