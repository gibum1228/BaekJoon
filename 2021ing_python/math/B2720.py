import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    for _ in range(int(IN())):
        C = int(IN())

        Q = C // 25
        C %= 25
        D = C // 10
        C %= 10
        N = C // 5
        C %= 5
        P = C

        print(Q, D, N, P)