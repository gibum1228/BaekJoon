import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, IN().split())

    print(min(N, M) // 2)