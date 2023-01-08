import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    arr = []

    for _ in range(int(IN())):
        s, e = map(int, IN().split())

        arr.append((s, e))

    time = 0
    for a in sorted(arr):
        s, e = a

        if time < s:
            time = s
        time += e

    print(time)