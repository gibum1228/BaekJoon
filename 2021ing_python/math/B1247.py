import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    for _ in range(3):
        N = int(IN())
        arr = [int(IN()) for _ in range(N)]

        what = sum(arr)
        if what == 0:
            print("0")
        elif what < 0:
            print("-")
        else:
            print("+")