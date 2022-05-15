import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N, K = map(int, IN().split())
    A = list(map(int, IN().rstrip().split()))
    sort_A = sorted(A)
    M = {}
    for i, x in enumerate(A):
        M[x] = i
    count = 0
    results = -1

    for i in range(N - 1, -1, -1):
        if A[i] != sort_A[i]:
            change_num, change_index = A[i], M[sort_A[i]]
            A[i], A[M[sort_A[i]]] = sort_A[i], A[i] # 5, 1

            M[change_num] = change_index
            M[A[i]] = i

            count += 1
            if count == K:
                results = f"{A[M[change_num]]} {A[i]}"

    print(results)