import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, IN().split())
    A, B = [list(map(int, IN().split())) for _ in range(N)], [list(map(int, IN().split())) for _ in range(N)]
    result = [[0 for _ in range(M)] for _ in range(N)]

    for r in range(N):
        for c in range(M):
            result[r][c] = A[r][c] + B[r][c]

    for arr in result:
        print(*arr)