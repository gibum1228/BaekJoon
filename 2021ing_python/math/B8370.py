import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    n1, k1, n2, k2 = map(int, IN().split())

    print((n1 * k1) + (n2 * k2))