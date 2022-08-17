import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    w, h = map(int, IN().split())
    res = w + h - (w ** 2 + h ** 2) ** 0.5
    print(res)