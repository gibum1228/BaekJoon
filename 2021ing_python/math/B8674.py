import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    a, b = map(int, IN().split())

    if a % 2 and b % 2:
        print(min(a, b))
    else:
        print(0)