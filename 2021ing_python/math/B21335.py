import sys
from math import pi

IN = sys.stdin.readline

if __name__ == "__main__":
    n = int(IN())
    print((n / pi) ** 0.5 * 2 * pi)