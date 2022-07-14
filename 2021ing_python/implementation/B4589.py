import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N = int(IN())
    result = "Gnomes:"

    for _ in range(N):
        trigger = False
        a, b, c = map(int, IN().split())

        if a >= b >= c or a <= b <= c:
            trigger = True

        if trigger:
            result += "\nOrdered"
        else:
            result += "\nUnordered"

    print(result)