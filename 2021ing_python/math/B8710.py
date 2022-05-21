import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    k, w, m = map(int, IN().split())

    if w <= k:
        print(0)
    else:
        if (w - k) % m == 0:
            print((w - k) // m)
        else:
            print((w - k) // m + 1)