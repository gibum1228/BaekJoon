import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    D, H, W = map(int, IN().split())

    R = D / ((H**2 + W**2)**0.5)
    print(int(H * R), int(W * R))