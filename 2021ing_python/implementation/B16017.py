import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    l = [int(IN()) for _ in range(4)]
    print('ignore' if l[0] > 7 < l[3] and l[1] == l[2] else 'answer')