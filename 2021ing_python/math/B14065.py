import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    x = float(input())
    ans = 100.0 / ((1.609344 / 3.785411784) * x)
    print("%.6f" % ans)