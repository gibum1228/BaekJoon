import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N = int(IN())
    A = list(map(int, IN().rstrip().split()))
    B = list(map(int, IN().rstrip().split()))
    sort_A = sorted(A)
    M = {}
    for i, x in enumerate(A):
        M[x] = i
    result_trigger = False

    for i in range(N - 1, -1, -1):
        if A == B:
            result_trigger = True
            break

        if A[i] != sort_A[i]:
            change_num, change_index = A[i], M[sort_A[i]]
            A[i], A[M[sort_A[i]]] = sort_A[i], A[i] # 5, 1

            M[change_num] = change_index
            M[A[i]] = i

    print(1) if result_trigger else print(0)