import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    ax, ay, az = map(int, IN().split())
    cx, cy, cz = map(int, IN().split())

    print(cx - az, cy // ay, cz - ax)