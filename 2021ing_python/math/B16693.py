import sys
from math import pi

IN = sys.stdin.readline

if __name__ == "__main__":
    A1, P1 = map(int, IN().split())
    R1, P2 = map(int, IN().split())

    if P1 / A1 < P2 / (R1 ** 2 * pi):
        print("Slice of pizza")
    else:
        print("Whole pizza")