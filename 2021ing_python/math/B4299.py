import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    S, M = map(int, IN().split())
    if S + M < 0 or S - M < 0 or (S + M) % 2:
        print(-1)
    else:
        a = (S + M) // 2
        b = S - a
        print(max(a, b), min(a, b))