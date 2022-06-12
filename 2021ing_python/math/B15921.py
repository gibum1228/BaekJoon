import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N = int(IN())
    if N:
        arr = list(map(int, IN().rstrip().split()))

        print("%.2f" % (sum(arr) / N / (sum(arr) / N)))
    else:
        print("divide by zero")