import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N = int(IN())

    for i in range(1, N + 1):
        if i % 2 == 0:
            print(" ", end="")
        for j in range(1, N + 1):
            print("* ", end="")
        print()