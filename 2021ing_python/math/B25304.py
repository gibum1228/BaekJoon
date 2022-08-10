import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    X = int(IN())
    N = int(IN())

    for _ in range(N):
        price, count = map(int, IN().split())

        X -= (price * count)

    print("Yes" if X == 0 else "No")