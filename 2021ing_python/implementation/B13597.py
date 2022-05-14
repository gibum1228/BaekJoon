import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    A, B = map(int, IN().split())

    print(max(A, B))