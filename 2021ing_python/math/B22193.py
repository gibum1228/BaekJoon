import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, IN().split())
    a = int(IN())
    b = int(IN())
    print(a * b)