import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    a, b, c = map(int, IN().split())

    h, j = [], []

    for i in [a, b, c]:
        if i % 2 == 0:
            j.append(i)
        else:
            h.append(i)

    arr = h if h else j
    num = 1
    for i in arr:
        num *= i
    print(num)