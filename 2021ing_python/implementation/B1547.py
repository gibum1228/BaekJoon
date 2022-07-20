import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N = int(IN())

    cups = [1, 2, 3]
    for _ in range(N):
        x, y = map(int, IN().split())

        xi = cups.index(x)
        yi = cups.index(y)

        cups[xi], cups[yi] = cups[yi], cups[xi]

    print(cups[0])