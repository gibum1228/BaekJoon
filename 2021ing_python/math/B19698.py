import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N, W, H, L = map(int, IN().split())

    result = (W // L) * (H // L)

    print(N if result > N else result)