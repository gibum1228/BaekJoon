import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N, K = map(int, IN().split())
    A = list(map(int, IN().rstrip().split()))
    count = 0
    trigger = True

    for i in range(N-1, 0, -1):
        max_num, max_index = A[0], 0

        for j in range(1, i + 1):
            if A[j] > max_num:
                max_num, max_index = A[j], j

        if A[i] != A[max_index]:
            A[i], A[max_index] = A[max_index], A[i]
            count += 1

        if count == K:
            trigger = False
            print(*A)

    if trigger:
        print(-1)