import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N = int(IN())
    A, B = map(int, IN().split())

    result = (A // 2) + B

    print(result if result <= N else N)