import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    X = int(IN())
    Y = int(IN())
    Z = int(IN())

    if X + Y > Z:
        print(0)
    else:
        print(1)