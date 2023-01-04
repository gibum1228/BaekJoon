import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N = int(IN())
    arange = N*5

    for r in range(arange):
        for c in range(arange):
            if c < N or c >= arange-N or r >= arange-N or N*3-N <= r < N*3:
                print('@', end='')
            else:
                print(' ', end='')
        print()