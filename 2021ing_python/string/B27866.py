import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    S = IN().rstrip()
    N = int(IN())

    print(S[N-1])