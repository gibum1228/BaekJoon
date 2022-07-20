import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    a, b = map(int, IN().split())
    a -= 1
    b -= 1

    print(abs(a // 4 - b // 4) + abs(a % 4 - b % 4))