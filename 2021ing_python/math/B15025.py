import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    l, r = map(int, IN().split())

    if l == 0 and r == 0:
        print("Not a moose")
    elif l == r:
        print(f"Even {l * 2}")
    else:
        print(f"Odd {max(l, r) * 2}")