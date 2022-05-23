import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    A1 = int(IN())
    A2 = int(IN())
    A3 = int(IN())

    r1 = A2*2 + A3*4
    r2 = A1*2 + A3*2
    r3 = A1*4 + A2*2

    print(min(r1, r2, r3))