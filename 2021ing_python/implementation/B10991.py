import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    n = int(IN())

    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * (i - 1) + "*")