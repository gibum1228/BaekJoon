import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N = int(IN())

    print(int(N * 0.78), int((N * 0.8) + (N * 0.2 * 0.78)))