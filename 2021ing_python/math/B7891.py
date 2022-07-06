import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    for _ in range(int(IN())):
        print(sum(map(int, IN().rstrip().split())))