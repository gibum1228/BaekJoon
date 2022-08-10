import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    n1, n2, n3 = map(int, IN().split())
    print((n1 + 1) * (n2 + 1) // (n3 + 1) - 1)
