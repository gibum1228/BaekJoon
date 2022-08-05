import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    n = int(IN())
    sum = 0

    for i in range(n):
        sum += int(IN())

    print(sum - (n - 1))