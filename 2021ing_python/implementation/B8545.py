import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    print("".join(list(IN().rstrip())[-1::-1]))