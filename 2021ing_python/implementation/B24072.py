import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    A, B, C = map(int, IN().split())

    if A <= C < B:
        print(1)
    else:
        print(0)