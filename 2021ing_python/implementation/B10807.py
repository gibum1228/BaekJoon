import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N = int(IN())
    score = list(map(int, IN().split()))
    focus = int(IN())

    print(score.count(focus))
