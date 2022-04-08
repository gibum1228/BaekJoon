import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    Y = int(IN())
    M = int(IN())

    print(M + (M - Y))