import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    n = int(IN())

    print(n*(n-1)//2)
    print(2)