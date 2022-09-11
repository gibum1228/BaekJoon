import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    arr = []
    s = ""

    for _ in range(int(IN())):
        arr.append(int(IN()))

    arr.sort()

    for x in arr:
        s += str(x) + "\n"

    print(s)