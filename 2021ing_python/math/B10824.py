import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    A, B, C, D = map(str, IN().split())

    print(int(A + B) + int(C + D))