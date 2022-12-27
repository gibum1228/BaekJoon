import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N = int(IN())
    arr = [[0 for _ in range(5*N)] for __ in range(5*N)]
    max_limit = N*5 - N

    for r in range(N*5):
        for c in range(N*5):
            if r < N or c < N or r >= max_limit or c >= max_limit:
                arr[r][c] = True

    for r in range(N*5):
        for c in range(N*5):
            if arr[r][c]:
                print("@", end='')
            else:
                print(" ", end='')
        print()