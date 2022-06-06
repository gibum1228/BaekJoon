import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    A, B = map(int, IN().split())
    C = int(IN())

    print(A + B - 2 * C if A + B >= 2 * C else A + B)