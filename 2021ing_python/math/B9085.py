import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    for _ in range(int(IN())):
        N = int(IN())
        print(sum(list(map(int, IN().rstrip().split()))))