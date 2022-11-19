import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    for _ in range(int(IN())):
        x, y = map(int, IN().split())

        if y <= x:
            print("MMM BRAINS")
        else:
            print("NO BRAINS")