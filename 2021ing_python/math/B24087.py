import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    S = int(IN())
    A = int(IN())
    B = int(IN())

    if A >= S:
        print(250)
    else:
        if (S - A) % B == 0:
            print(250 + 100 * ((S - A) // B))
        else:
            print(250 + 100 * ((S - A) // B + 1))