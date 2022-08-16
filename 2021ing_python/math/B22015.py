import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    A, B, C = map(int, IN().split())

    max_num = max([A, B, C])

    print((max_num - A) +  (max_num - B) + (max_num - C))