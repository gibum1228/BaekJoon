import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N, A, B, C, D = map(int, input().split())
    A = (N // A + (1 if N % A else 0)) * B
    C = (N // C + (1 if N % C else 0)) * D

    print(min(A, C))