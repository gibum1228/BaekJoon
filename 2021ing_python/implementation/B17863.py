import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N = IN().rstrip()

    if "555" == N[:3]:
        print("YES")
    else:
        print("NO")