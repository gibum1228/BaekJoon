import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    A, B = map(int, IN().split())
    M = (B - A) / 400

    print(1 / (1 + 10**M))