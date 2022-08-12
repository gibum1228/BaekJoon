import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    tmp = list(map(int, IN().split()))
    print(sum(tmp) * 5)