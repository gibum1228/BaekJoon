import sys
from math import pi

IN = sys.stdin.readline

if __name__ == "__main__":
    a = int(IN())

    print((a / pi) ** 0.5 * 2 * pi)