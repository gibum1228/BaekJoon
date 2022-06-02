import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    S, T, D = map(int, IN().split())
    print(D // (S*2) * T)